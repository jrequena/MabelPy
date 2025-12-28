<?php

declare(strict_types=1);

namespace App\Infrastructure\Mapper;

use App\Domain\Enum\UserStatus;
use App\Domain\User;
use App\Domain\ValueObject\Email;

final class UserMapper
{
    public static function fromArray(array $data): User
    {
        return new User(

            $data['id'],

            isset($data['email']) ? new Email($data['email']) : null,

            new \DateTimeImmutable($data['created_at']),

            $data['active'],

            UserStatus::from($data['status']),

        );
    }

    public static function toArray(User $entity): array
    {
        return [

            'id' => $entity->id,

            'email' => $entity->email?->value,

            'created_at' => $entity->created_at->format(\DateTimeInterface::ATOM),

            'active' => $entity->active,

            'status' => $entity->status->value,

        ];
    }
}
