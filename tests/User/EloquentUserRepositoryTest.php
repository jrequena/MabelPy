<?php

declare(strict_types=1);

namespace App\Tests\User;

use App\Domain\Enum\UserStatus;
use App\Domain\User;
use App\Infrastructure\Persistence\Eloquent\EloquentUserRepository;
use App\Tests\TestCase;
use App\Tests\RefreshDatabase;

final class EloquentUserRepositoryTest extends TestCase
{
    use RefreshDatabase;

    private EloquentUserRepository $repository;

    protected function setUp(): void
    {
        parent::setUp();
        $this->repository = $this->app(EloquentUserRepository::class);
    }

    public function test_can_save_and_find_entity(): void
    {
        // 1. Create domain entity
        $entity = new User(
            1,
            'sample',
            'sample',
            UserStatus::ACTIVE,
            new \DateTimeImmutable(),
            [],
        );

        // 2. Save via repository
        $this->repository->save($entity);

        // 3. Find and verify
        $found = $this->repository->findById($entity->id);

        $this->assertNotNull($found);
        $this->assertEquals($entity->id, $found->id);
    }

    public function test_can_delete_entity(): void
    {
        $entity = new User(
            1,
            'sample',
            'sample',
            UserStatus::ACTIVE,
            new \DateTimeImmutable(),
            [],
        );

        $this->repository->save($entity);
        $this->repository->delete($entity->id);

        $found = $this->repository->findById($entity->id);
        $this->assertNull($found);
    }
}
