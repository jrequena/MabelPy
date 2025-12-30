<?php

declare(strict_types=1);

namespace App\Tests;

use App\Domain\Repository\PostRepository;
use App\Domain\UseCase\Post\CreateUser\CreateUserUseCase;
use PHPUnit\Framework\TestCase;
final class CreateUserUseCaseTest extends TestCase
{
    public function test_can_be_instantiated(): void
    {
        $repository = $this->createMock(PostRepository::class);
        $useCase = new CreateUserUseCase($repository);
        
        $this->assertInstanceOf(CreateUserUseCase::class, $useCase);
    }
}
