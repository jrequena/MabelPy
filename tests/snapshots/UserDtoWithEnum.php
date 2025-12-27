<?php
declare(strict_types=1);

namespace App\Dto;


use DateTimeImmutable;

use App\Enum\UserStatus;


final class UserDto
{
    public function __construct(

        public readonly int $id,

        public readonly ?string $email = null,

        public readonly DateTimeImmutable $created_at,

        public readonly bool $active = true,

        public readonly UserStatus $status = UserStatus::ACTIVE,

    ) {

        if ($id <= 0) {
            throw new \InvalidArgumentException("id must be positive");
        }

        if ($email !== null && !filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new \InvalidArgumentException("email must be a valid email");
        }

    }
}