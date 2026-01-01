<?php

declare(strict_types=1);

namespace App\Tests;

use PHPUnit\Framework\TestCase as BaseTestCase;

abstract class TestCase extends BaseTestCase
{
    protected function app(string $abstract)
    {
        if (function_exists('app')) {
            return app($abstract);
        }
        
        return new $abstract();
    }
}
