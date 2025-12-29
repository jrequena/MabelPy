<?php

declare(strict_types=1);

namespace App\Domain;

use App\Domain\Enum\UserStatus;

final class User
{
    public function __construct(

        public readonly int $id,

        public readonly string $name,

        public readonly UserStatus $status,

    ) {
    }
}
