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
                $type = $parameter->getType();
                if ($type instanceof \ReflectionNamedType && !$type->isBuiltin()) {
                    $dependencies[] = $this->app($type->getName());
                } else {
                    $dependencies[] = null;
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
