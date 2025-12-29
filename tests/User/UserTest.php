<?php

declare(strict_types=1);

namespace App\Tests;

use PHPUnit\Framework\TestCase;
use App\Domain\User;


final class UserTest extends TestCase
{
    public function test_can_be_instantiated(): void
    {
        $entity = new User(

            1,

            'sample',

            'sample',

            null,

            new \DateTimeImmutable(),

        );

        $this->assertInstanceOf(User::class, $entity);
    }
}
