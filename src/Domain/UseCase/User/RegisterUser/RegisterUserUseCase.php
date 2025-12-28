<?php

declare(strict_types=1);

namespace App\Domain\UseCase\User\RegisterUser;

use App\Domain\Repository\UserRepository;
final class RegisterUserUseCase
{
    public function __construct(
        private readonly UserRepository $repository
    ) {
    }

    public function execute(RegisterUserRequest $request): RegisterUserResponse
    {
        // TODO: Implement business logic
        return new RegisterUserResponse();
    }
}
