<?php

namespace App\Tests;

use PHPUnit\Framework\TestCase as BaseTestCase;
use Illuminate\Database\Capsule\Manager as Capsule;
use Illuminate\Events\Dispatcher;
use Illuminate\Container\Container;

abstract class TestCase extends BaseTestCase
{
    protected function setUp(): void
    {
        parent::setUp();

        $capsule = new Capsule();

        $capsule->addConnection([
            'driver' => 'sqlite',
            'database' => ':memory:',
            'prefix' => '',
        ]);

        $capsule->setEventDispatcher(new Dispatcher(new Container()));
        $capsule->setAsGlobal();
        $capsule->bootEloquent();

        $this->setUpDatabase();
    }

    protected function setUpDatabase(): void
    {
        Capsule::schema()->create('posts', function ($table) {
            $table->uuid('id')->primary();
            $table->string('title');
            $table->text('content');
            $table->timestamps();
        });

        Capsule::schema()->create('users', function ($table) {
            $table->uuid('id')->primary();
            $table->string('email');
            $table->string('name');
            $table->timestamps();
        });
    }
}
