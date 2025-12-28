<?php

declare(strict_types=1);

namespace App\Domain;

use DateTimeImmutable;

use App\Domain\Enum\UserStatus;

use App\Domain\ValueObject\Email;

final class User
{
    public function __construct(

        public readonly int $id,

        public readonly ?Email $email = null,

        public readonly DateTimeImmutable $created_at,

        public readonly bool $active = true,

        public readonly UserStatus $status = UserStatus::ACTIVE,

    ) {

        if ($id <= 0) { throw new \InvalidArgumentException("id must be positive"); }

    }
}
