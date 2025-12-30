<?php

declare(strict_types=1);

namespace {{ namespace }};

namespace Database\Seeders;

use {{ model_import }};
use Illuminate\Database\Seeder;

final class {{ class_name }}Seeder extends Seeder
{
    public function run(): void
    {
        {{ class_name }}::factory()->count(10)->create();
    }
}
