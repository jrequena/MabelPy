<?php

declare(strict_types=1);

namespace App\Domain\UseCase\User\RegisterUser;

final readonly class RegisterUserResponse
{
    public function __construct(

        public int $id,

        public bool $success,

    ) {
    }
}
