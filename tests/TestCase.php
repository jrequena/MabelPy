<?php

declare(strict_types=1);

namespace App\Tests;

use PHPUnit\Framework\TestCase as BaseTestCase;
use Illuminate\Database\Capsule\Manager as Capsule;
use ReflectionClass;

/**
 * Mock RefreshDatabase trait
 */
trait RefreshDatabase {
    protected function setUpRefreshDatabase(): void {}
}

abstract class TestCase extends BaseTestCase
{
    private static bool $initialized = false;
    protected static $container = null;

    protected function setUp(): void
    {
        parent::setUp();
        
        $this->initializeEnvironment();

        if (method_exists($this, 'setUpRefreshDatabase')) {
            $this->setUpRefreshDatabase();
        }
    }

    private function initializeEnvironment(): void
    {
        if (self::$initialized) {
            return;
        }

        if (class_exists('Illuminate\Container\Container')) {
            $container = new \Illuminate\Container\Container();
            self::$container = $container;
        } else {
            // Minimal container if illuminate/container is missing
            self::$container = new class {
                private $instances = [];
                public function instance($abstract, $instance) { $this->instances[$abstract] = $instance; return $instance; }
                public function make($abstract) { return $this->instances[$abstract] ?? null; }
                public function has($abstract) { return isset($this->instances[$abstract]); }
                public function singleton($abstract, $concrete) { $this->instances[$abstract] = $concrete(); }
                public function alias($abstract, $alias) { if (isset($this->instances[$abstract])) $this->instances[$alias] = &$this->instances[$abstract]; }
            };
        }

        $capsule = new Capsule(self::$container instanceof \Illuminate\Container\Container ? self::$container : null);

        $capsule->addConnection([
            'driver' => 'sqlite',
            'database' => ':memory:',
            'prefix' => '',
        ]);

        if (class_exists('Illuminate\Events\Dispatcher')) {
            $capsule->setEventDispatcher(new \Illuminate\Events\Dispatcher(self::$container instanceof \Illuminate\Container\Container ? self::$container : null));
        }

        $capsule->setAsGlobal();
        $capsule->bootEloquent();
        
        if (class_exists('Illuminate\Support\Facades\Facade')) {
            \Illuminate\Support\Facades\Facade::setFacadeApplication(self::$container instanceof \Illuminate\Container\Container ? self::$container : null);
            if (method_exists(self::$container, 'instance')) {
                self::$container->instance('db', $capsule->getDatabaseManager());
            }
        }

        $this->setUpDatabase();
        
        self::$initialized = true;
    }

    protected function setUpDatabase(): void
    {
        Capsule::schema()->create('posts', function ($table) {
            $table->increments('id');
            $table->string('title');
            $table->text('content');
            $table->integer('user_id')->nullable();
            $table->timestamps();
        });

        Capsule::schema()->create('users', function ($table) {
            $table->increments('id');
            $table->string('email');
            $table->string('name');
            $table->string('status')->default('active');
            $table->timestamps();
        });
    }

    protected function app(string $abstract)
    {
        $this->initializeEnvironment();

        if (self::$container && method_exists(self::$container, 'has') && self::$container->has($abstract)) {
            return self::$container->make($abstract);
        }

        try {
            $reflection = new ReflectionClass($abstract);
            
            if ($reflection->isInterface()) {
                return $this->createMock($abstract);
            }

            $constructor = $reflection->getConstructor();
            
            if (null === $constructor) {
                $instance = new $abstract();
            } else {
                $parameters = $constructor->getParameters();
                $dependencies = [];
                
                foreach ($parameters as $parameter) {
                    if ($parameter->isDefaultValueAvailable()) {
                        $dependencies[] = $parameter->getDefaultValue();
                        continue;
                    }

                    $type = $parameter->getType();
                    if ($type instanceof \ReflectionNamedType && !$type->isBuiltin()) {
                        $dependencies[] = $this->app($type->getName());
                    } else {
                        $dependencies[] = ($type instanceof \ReflectionNamedType && $type->getName() === 'array') ? [] : null;
                    }
                }
                
                $instance = $reflection->newInstanceArgs($dependencies);
            }
            
            if (self::$container && method_exists(self::$container, 'instance')) {
                self::$container->instance($abstract, $instance);
            }
            return $instance;
            
        } catch (\Throwable $e) {
            if (class_exists($abstract)) {
                $reflection = new ReflectionClass($abstract);
                if (!$reflection->isFinal()) {
                    return $this->createMock($abstract);
                }
            }
            throw $e;
        }
    }
}
