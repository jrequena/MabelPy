<?php

declare(strict_types=1);

namespace App\Tests\User;

use App\Domain\Repository\UserRepository;
use App\Domain\UseCase\User\UpdateUserEmail\UpdateUserEmailUseCase;

use App\Tests\TestCase;
use App\Tests\RefreshDatabase;

final class UpdateUserEmailUseCaseTest extends TestCase
{
    use RefreshDatabase;

    public function test_can_be_instantiated(): void
    {
        $useCase = $this->app(UpdateUserEmailUseCase::class);
        $this->assertInstanceOf(UpdateUserEmailUseCase::class, $useCase);
    }
}
