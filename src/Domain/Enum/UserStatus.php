<?php

declare(strict_types=1);

namespace App\Domain\Enum;

enum UserStatus: string
{

    case ACTIVE = 'active';

    case BLOCKED = 'blocked';

    case DELETED = 'deleted';

}
