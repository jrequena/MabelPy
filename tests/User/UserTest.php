<?php

declare(strict_types=1);

namespace App\Tests;

use App\Domain\User;
use PHPUnit\Framework\TestCase;

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
            [],
        );

        $this->assertInstanceOf(User::class, $entity);
    }
}
