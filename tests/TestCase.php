<?php

declare(strict_types=1);

namespace App\Tests;

use PHPUnit\Framework\TestCase as BaseTestCase;

/**
 * Mock RefreshDatabase trait if it doesn't exist
 */
if (!trait_exists('Illuminate\Foundation\Testing\RefreshDatabase')) {
    trait RefreshDatabase {
        protected function setUpRefreshDatabase(): void {}
    }
}

/**
 * Mock Eloquent Model if it doesn't exist
 */
if (!class_exists('Illuminate\Database\Eloquent\Model')) {
    eval('namespace Illuminate\Database\Eloquent { 
        abstract class Model {
            public function __call($method, $args) { return $this; }
            public static function __callStatic($method, $args) { return new static; }
            public function toArray() { return []; }
            public function belongsTo($related) { return new class { public function __call($n, $a) { return $this; } }; }
        }
    }');
}

/**
 * Mock DB facade if it doesn't exist
 */
if (!class_exists('Illuminate\Support\Facades\DB')) {
    eval('namespace Illuminate\Support\Facades { 
        class DB {
            public static function transaction($callback) { return $callback(); }
            public static function __callStatic($method, $args) { return null; }
        }
    }');
}

abstract class TestCase extends BaseTestCase
{
    protected function setUp(): void
    {
        parent::setUp();
        
        if (method_exists($this, 'setUpRefreshDatabase')) {
            $this->setUpRefreshDatabase();
        }

        if (class_exists('Illuminate\Support\Facades\Facade')) {
            try {
                if (!function_exists('app') || !(@\app() instanceof \Illuminate\Container\Container)) {
                    $container = new \Illuminate\Container\Container();
                    $dbMock = new class {
                        public function transaction($callback) { return $callback(); }
                        public function connection($n = null) { return $this; }
                        public function getName() { return 'default'; }
                        public function __call($m, $a) { return $this; }
                    };
                    $container->singleton('db', fn() => $dbMock);
                    $container->alias('db', 'db.factory');
                    \Illuminate\Support\Facades\Facade::setFacadeApplication($container);
                    
                    if (class_exists('Illuminate\Database\Eloquent\Model')) {
                        \Illuminate\Database\Eloquent\Model::setConnectionResolver($dbMock);
                    }
                }
            } catch (\Throwable $e) {
                // Ignore if already set or other issues
            }
        }
    }

    protected function app(string $abstract)
    {
        if (function_exists('app')) {
            return \app($abstract);
        }
        
        try {
            $reflection = new \ReflectionClass($abstract);
            
            if ($reflection->isInterface()) {
                return $this->createMock($abstract);
            }

            $constructor = $reflection->getConstructor();
            
            if (null === $constructor) {
                return new $abstract();
            }
            
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
            
            return $reflection->newInstanceArgs($dependencies);
        } catch (\Throwable $e) {
            if (class_exists($abstract)) {
                $reflection = new \ReflectionClass($abstract);
                if (!$reflection->isFinal()) {
                    return $this->createMock($abstract);
                }
            }
            throw $e;
        }
    }
}
