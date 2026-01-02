<?php

declare(strict_types=1);

namespace App\Tests\Post;

use App\Domain\Post;

use App\Tests\TestCase;

final class PostTest extends TestCase
{
    public function test_can_be_instantiated(): void
    {
        $entity = new Post(
            1,
            'sample',
            'sample',
            null,
        );

        $this->assertInstanceOf(Post::class, $entity);
    }
}
