<?php

declare(strict_types=1);

namespace App\Domain\Repository;

use App\Domain\User;

interface UserRepository
{
    public function save(User $entity): void;
    public function findById(int $id): ?User;
    public function delete(int $id): void;
}
