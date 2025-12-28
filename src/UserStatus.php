<?php
declare(strict_types=1);

namespace App\Enum;

final enum UserStatus: string
{

    case ACTIVE = 'active';

    case BLOCKED = 'blocked';

    case DELETED = 'deleted';

}
