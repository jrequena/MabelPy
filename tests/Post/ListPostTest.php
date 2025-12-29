<?php

declare(strict_types=1);

namespace App\Tests;

use PHPUnit\Framework\TestCase;
use App\Domain\Repository\PostRepository;
use App\Domain\UseCase\ListPost;

final class ListPostTest extends TestCase
{
    public function test_can_be_instantiated(): void
    {
        $repository = $this->createMock(PostRepository::class);
        $useCase = new ListPost($repository);
        
        $this->assertInstanceOf(ListPost::class, $useCase);
    }
}