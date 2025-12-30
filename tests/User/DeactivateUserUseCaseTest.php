<?php

declare(strict_types=1);

namespace App\Tests\User;

use App\Domain\Repository\UserRepository;
use App\Domain\UseCase\User\DeactivateUser\DeactivateUserUseCase;
use PHPUnit\Framework\TestCase;

final class DeactivateUserUseCaseTest extends TestCase
{
    public function test_can_be_instantiated(): void
    {
        $repository = $this->createMock(UserRepository::class);
        $useCase = new DeactivateUserUseCase($repository);
        
        $this->assertInstanceOf(DeactivateUserUseCase::class, $useCase);
    }
}
