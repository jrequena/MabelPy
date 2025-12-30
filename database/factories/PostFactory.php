<?php

declare(strict_types=1);

namespace <class 'jinja2.utils.Namespace'>;

namespace Database\Factories;

use App\Infrastructure\Persistence\Eloquent\Post;
use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Infrastructure\Persistence\Eloquent\Post>
 */
final class PostFactory extends Factory
{
    protected $model = Post::class;

    public function definition(): array
    {
        return [
            'title' => fake()->word(),
            'content' => fake()->word(),
            'user_id' => \Infrastructure\Persistence\Eloquent\User::factory(),
        ];
    }
}
