<?php

declare(strict_types=1);

namespace App\Tests\Post;

use App\Domain\Post;
use App\Infrastructure\Mapper\PostMapper;
use PHPUnit\Framework\TestCase;

final class PostMapperTest extends TestCase
{
    public function test_can_map_from_array(): void
    {
        $data = [
            'id' => 1,
            'title' => 'sample',
            'content' => 'sample',
            'user' => null,
        ];

        $entity = PostMapper::fromArray($data);

        $this->assertInstanceOf(Post::class, $entity);
    }

    public function test_can_map_to_array(): void
    {
        $entity = new Post(
            1,
            'sample',
            'sample',
            null,
        );

        $data = PostMapper::toArray($entity);

        $this->assertEquals(1, $data['id']);
        $this->assertEquals('sample', $data['title']);
        $this->assertEquals('sample', $data['content']);
        $this->assertEquals(null, $data['user']);
    }
}
