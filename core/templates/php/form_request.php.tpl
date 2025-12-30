<?php

declare(strict_types=1);

namespace {{ namespace }};

use Illuminate\Foundation\Http\FormRequest;

class {{ class_name }} extends FormRequest
{
    public function authorize(): bool
    {
        return true;
    }

    public function rules(): array
    {
        return [
            {% for field, rules in validation_rules.items() %}
            '{{ field }}' => [{% for rule in rules %}'{{ rule }}'{% if not loop.last %}, {% endif %}{% endfor %}],
            {% endfor %}
        ];
    }
}
