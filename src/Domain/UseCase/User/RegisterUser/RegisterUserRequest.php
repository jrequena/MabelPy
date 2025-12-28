<?php

declare(strict_types=1);

namespace App\Domain\UseCase\User\RegisterUser;

final readonly class RegisterUserRequest
{
    public function __construct(

        public string $email,

        public string $name,

    ) {
    }
}
