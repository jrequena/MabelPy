<?php

declare(strict_types=1);

namespace App\Tests;

use PHPUnit\Framework\TestCase;
use App\Domain\Repository\PostRepository;
use App\Domain\UseCase\UpdatePost;

final class UpdatePostTest extends TestCase
{
    public function test_can_be_instantiated(): void
    {
        $repository = $this->createMock(PostRepository::class);
        $useCase = new UpdatePost($repository);
        
        $this->assertInstanceOf(UpdatePost::class, $useCase);
    }
}