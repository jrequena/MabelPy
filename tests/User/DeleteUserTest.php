<?php

declare(strict_types=1);

namespace App\Tests;

use PHPUnit\Framework\TestCase;
use App\Domain\Repository\UserRepository;
use App\Domain\UseCase\DeleteUser;

final class DeleteUserTest extends TestCase
{
    public function test_can_be_instantiated(): void
    {
        $repository = $this->createMock(UserRepository::class);
        $useCase = new DeleteUser($repository);
        
        $this->assertInstanceOf(DeleteUser::class, $useCase);
    }
}