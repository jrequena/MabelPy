<?php

declare(strict_types=1);

namespace App\Tests\User;

use App\Domain\Repository\UserRepository;
use App\Domain\UseCase\User\CreateUser\CreateUserUseCase;

use App\Tests\TestCase;
use App\Tests\RefreshDatabase;

final class CreateUserUseCaseTest extends TestCase
{
    use RefreshDatabase;

    public function test_can_be_instantiated(): void
    {
        $useCase = $this->app(CreateUserUseCase::class);
        $this->assertInstanceOf(CreateUserUseCase::class, $useCase);
    }
}
