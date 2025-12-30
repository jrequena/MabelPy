<?php

declare(strict_types=1);

namespace App\Tests;

use App\Domain\Repository\UserRepository;
use App\Domain\UseCase\User\UpdateUserEmail\UpdateUserEmailUseCase;
use PHPUnit\Framework\TestCase;
final class UpdateUserEmailUseCaseTest extends TestCase
{
    public function test_can_be_instantiated(): void
    {
        $repository = $this->createMock(UserRepository::class);
        $useCase = new UpdateUserEmailUseCase($repository);
        
        $this->assertInstanceOf(UpdateUserEmailUseCase::class, $useCase);
    }
}
