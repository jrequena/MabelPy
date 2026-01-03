<?php

declare(strict_types=1);

namespace App\Tests\Post;

use App\Domain\Post;
use App\Infrastructure\Persistence\Eloquent\EloquentPostRepository;
use App\Tests\TestCase;

final class EloquentPostRepositoryTest extends TestCase
{
    private EloquentPostRepository $repository;

    protected function setUp(): void
    {
        parent::setUp();
        $this->repository = $this->app(EloquentPostRepository::class);
    }

    public function test_can_save_and_find_entity(): void
    {
        // 1. Create domain entity
        $entity = new Post(
            1,
            'sample',
            'sample',
            null,
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
        $entity = new Post(
            1,
            'sample',
            'sample',
            null,
        );

        $this->repository->save($entity);
        $this->repository->delete($entity->id);

        $found = $this->repository->findById($entity->id);
        $this->assertNull($found);
    }
}
