<?php

declare(strict_types=1);

namespace App\Tests\User;

use App\Domain\Enum\UserStatus;
use App\Domain\User;

use App\Tests\TestCase;

final class UserTest extends TestCase
{
    public function test_can_be_instantiated(): void
    {
        $entity = new User(
            1,
            'sample',
            'sample',
            UserStatus::ACTIVE,
            new \DateTimeImmutable(),
            [],
        );

        $this->assertInstanceOf(User::class, $entity);
    }
}
