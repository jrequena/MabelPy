<?php

declare(strict_types=1);

namespace App\Tests\User;

use App\Domain\User;
use App\Infrastructure\Mapper\UserMapper;
use PHPUnit\Framework\TestCase;

final class UserMapperTest extends TestCase
{
    public function test_can_map_from_array(): void
    {
        $data = [
            'id' => 1,
            'name' => 'sample',
            'email' => 'sample',
            'status' => null,
            'created_at' => '2023-01-01T00:00:00+00:00',
            'posts' => [],
        ];

        $entity = UserMapper::fromArray($data);

        $this->assertInstanceOf(User::class, $entity);
    }

    public function test_can_map_to_array(): void
    {
        $entity = new User(
            1,
            'sample',
            'sample',
            null,
            new \DateTimeImmutable('2023-01-01 00:00:00'),
            [],
        );

        $data = UserMapper::toArray($entity);

        $this->assertEquals(1, $data['id']);
        $this->assertEquals('sample', $data['name']);
        $this->assertEquals('sample', $data['email']);
        $this->assertEquals(null, $data['status']);
        $this->assertEquals('2023-01-01T00:00:00+00:00', $data['created_at']);
        $this->assertEquals([], $data['posts']);
    }
}
