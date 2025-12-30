<?php

declare(strict_types=1);

namespace App\Tests;

use App\Domain\Post;
use PHPUnit\Framework\TestCase;

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
