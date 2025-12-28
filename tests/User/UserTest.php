<?php

declare(strict_types=1);

namespace App\Tests;

use PHPUnit\Framework\TestCase;
use App\Domain\Enum\UserStatus;
use App\Domain\User;
use App\Domain\ValueObject\Email;


final class UserTest extends TestCase
{
    public function test_can_be_instantiated(): void
    {
        $entity = new User(

            1,

            new Email('test@example.com'),

            new \DateTimeImmutable(),

            true,

            UserStatus::ACTIVE,

        );

        $this->assertInstanceOf(User::class, $entity);
    }
}
