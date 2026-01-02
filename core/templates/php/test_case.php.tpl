<?php

declare(strict_types=1);

namespace {{ namespace }};

use PHPUnit\Framework\TestCase as BaseTestCase;

/**
 * Mock RefreshDatabase trait if it doesn't exist
 */
if (!trait_exists('Illuminate\Foundation\Testing\RefreshDatabase')) {
    trait RefreshDatabase {
        protected function setUpRefreshDatabase(): void {}
    }
} else {
    class_alias('Illuminate\Foundation\Testing\RefreshDatabase', 'App\Tests\RefreshDatabase');
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
    /**
     * Helper to mock app() if not in Laravel
     */
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
