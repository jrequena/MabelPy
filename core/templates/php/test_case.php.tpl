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
        
        // Manual instantiation for standalone (stubbed) using Reflection
        try {
            $reflection = new \ReflectionClass($abstract);
            $constructor = $reflection->getConstructor();
            
            if (null === $constructor) {
                return new $abstract();
            }
            
            $parameters = $constructor->getParameters();
            $dependencies = [];
            
            foreach ($parameters as $parameter) {
                $type = $parameter->getType();
                if ($type instanceof \ReflectionNamedType && !$type->isBuiltin()) {
                    $typeName = $type->getName();
                    $typeReflection = new \ReflectionClass($typeName);
                    if ($typeReflection->isFinal()) {
                        // If final, try to instantiate directly or just null if it fails
                        try {
                            $dependencies[] = new $typeName();
                        } catch (\Throwable $e) {
                            $dependencies[] = null;
                        }
                    } else {
                        $dependencies[] = $this->createMock($typeName);
                    }
                } else {
                    $dependencies[] = null;
                }
            }
            
            return $reflection->newInstanceArgs($dependencies);
        } catch (\Throwable $e) {
            $reflection = new \ReflectionClass($abstract);
            if ($reflection->isFinal()) {
                 // Final classes cannot be mocked, throw the original error or try to instantiate
                 throw $e;
            }
            return $this->createMock($abstract);
        }
    }
}
