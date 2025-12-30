<?php

declare(strict_types=1);

namespace <class 'jinja2.utils.Namespace'>;

namespace Database\Seeders;

use App\Infrastructure\Persistence\Eloquent\User;
use Illuminate\Database\Seeder;

final class UserSeeder extends Seeder
{
    public function run(): void
    {
        User::factory()->count(10)->create();
    }
}
