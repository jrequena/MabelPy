<?php

declare(strict_types=1);

namespace App\Tests;

use PHPUnit\Framework\TestCase;
use App\Domain\Enum\UserStatus;
use App\Domain\User;
use App\Domain\ValueObject\Email;
use App\Infrastructure\Mapper\UserMapper;

final class UserMapperTest extends TestCase
{
    public function test_can_map_from_array(): void
    {
        $data = [

            'id' => 1,

            'email' => 'test@example.com',

            'created_at' => '2023-01-01T00:00:00+00:00',

            'active' => true,

            'status' => 'ACTIVE',

        ];

        $entity = UserMapper::fromArray($data);

        $this->assertInstanceOf(User::class, $entity);
    }

    public function test_can_map_to_array(): void
    {
        $entity = new User(

            1,

            new Email('test@example.com'),

            new \DateTimeImmutable('2023-01-01 00:00:00'),

            true,

            UserStatus::ACTIVE,

        );

        $data = UserMapper::toArray($entity);


        $this->assertEquals(1, $data['id']);

        $this->assertEquals('test@example.com', $data['email']);

        $this->assertEquals('2023-01-01T00:00:00+00:00', $data['created_at']);

        $this->assertEquals(true, $data['active']);

        $this->assertEquals('ACTIVE', $data['status']);

    }
}
