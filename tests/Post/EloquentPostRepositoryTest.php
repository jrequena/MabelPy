<?php

declare(strict_types=1);

namespace App\Tests\Post;

use App\Domain\Post;
use App\Infrastructure\Persistence\Eloquent\EloquentPostRepository;
use App\Tests\TestCase;
use App\Tests\RefreshDatabase;

final class EloquentPostRepositoryTest extends TestCase
{
    use RefreshDatabase;

    private EloquentPostRepository $repository;

    protected function setUp(): void
    {
        parent::setUp();
        // Since we are in standalone, this app() will return a mock/stub
        $this->repository = $this->app(EloquentPostRepository::class);
    }

    public function test_can_be_instantiated(): void
    {
        $this->assertInstanceOf(EloquentPostRepository::class, $this->repository);
    }
}
