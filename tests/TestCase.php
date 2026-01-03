<?php

declare(strict_types=1);

namespace App\Tests;

use PHPUnit\Framework\TestCase as BaseTestCase;
use Illuminate\Database\Capsule\Manager as Capsule;
use Illuminate\Events\Dispatcher;
use Illuminate\Container\Container;
use Illuminate\Support\Facades\Facade;
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
    protected static ?Container $container = null;

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

        $container = new Container();
        self::$container = $container;

        $capsule = new Capsule($container);

        $capsule->addConnection([
            'driver' => 'sqlite',
            'database' => ':memory:',
            'prefix' => '',
        ]);

        $capsule->setEventDispatcher(new Dispatcher($container));
        $capsule->setAsGlobal();
        $capsule->bootEloquent();
        
        if (class_exists(Facade::class)) {
            Facade::setFacadeApplication($container);
            $container->instance('db', $capsule->getDatabaseManager());
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

        if (self::$container->has($abstract)) {
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
            
            self::$container->instance($abstract, $instance);
            return $instance;
            
        } catch (\Throwable $e) {
            return $this->createMock($abstract);
        }
    }
}
