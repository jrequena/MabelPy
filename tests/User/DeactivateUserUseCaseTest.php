<?php

declare(strict_types=1);

namespace App\Tests;

use PHPUnit\Framework\TestCase;
use App\Domain\Repository\UserRepository;
use App\Domain\UseCase\User\DeactivateUser\DeactivateUserUseCase;

final class DeactivateUserUseCaseTest extends TestCase
{
    public function test_can_be_instantiated(): void
    {
        $repository = $this->createMock(UserRepository::class);
        $useCase = new DeactivateUserUseCase($repository);
        
        $this->assertInstanceOf(DeactivateUserUseCase::class, $useCase);
    }
}