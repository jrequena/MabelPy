<?php

declare(strict_types=1);

namespace App\Tests\User;

use App\Domain\Repository\UserRepository;
use App\Domain\UseCase\User\DeactivateUser\DeactivateUserUseCase;

use App\Tests\TestCase;
use App\Tests\RefreshDatabase;

final class DeactivateUserUseCaseTest extends TestCase
{
    use RefreshDatabase;

    public function test_can_be_instantiated(): void
    {
        $useCase = $this->app(DeactivateUserUseCase::class);
        $this->assertInstanceOf(DeactivateUserUseCase::class, $useCase);
    }
}
