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
        
        // Manual instantiation for standalone
        return new $abstract(new class {
            public function __call($name, $args) { return $this; }
            public static function __callStatic($name, $args) { return new static; }
        });
    }
}
