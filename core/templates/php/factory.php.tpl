<?php

declare(strict_types=1);

namespace Database\Factories;

use {{ model_import }};
use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\{{ model_import }}>
 */
final class {{ class_name }}Factory extends Factory
{
    protected $model = {{ class_name }}::class;

    public function definition(): array
    {
        return [
{% for field in fields %}
            '{{ field.name }}' => {{ field.faker_line }},
{% endfor %}
        ];
    }
}
