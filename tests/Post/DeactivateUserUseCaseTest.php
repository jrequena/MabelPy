<?php

declare(strict_types=1);

namespace App\Tests;

use PHPUnit\Framework\TestCase;
use App\Domain\Repository\PostRepository;
use App\Domain\UseCase\Post\DeactivateUser\DeactivateUserUseCase;

final class DeactivateUserUseCaseTest extends TestCase
{
    public function test_can_be_instantiated(): void
    {
        $repository = $this->createMock(PostRepository::class);
        $useCase = new DeactivateUserUseCase($repository);
        
        $this->assertInstanceOf(DeactivateUserUseCase::class, $useCase);
    }
}