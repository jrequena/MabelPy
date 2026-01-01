<?php

declare(strict_types=1);

namespace {{ namespace }};

use PHPUnit\Framework\TestCase as BaseTestCase;

abstract class TestCase extends BaseTestCase
{
    /**
     * Helper to mock app() if not in Laravel
     */
    protected function app(string $abstract)
    {
        // Simple mock for non-Laravel environments or actual Laravel app()
        if (function_exists('app')) {
            return app($abstract);
        }
        
        return new $abstract();
    }
}
