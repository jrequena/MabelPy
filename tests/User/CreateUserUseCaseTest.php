<?php

declare(strict_types=1);

namespace App\Tests;

use PHPUnit\Framework\TestCase;
use App\Domain\Repository\UserRepository;
use App\Domain\UseCase\User\CreateUser\CreateUserUseCase;

final class CreateUserUseCaseTest extends TestCase
{
    public function test_can_be_instantiated(): void
    {
        $repository = $this->createMock(UserRepository::class);
        $useCase = new CreateUserUseCase($repository);
        
        $this->assertInstanceOf(CreateUserUseCase::class, $useCase);
    }
}