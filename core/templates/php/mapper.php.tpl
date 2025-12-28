<?php

declare(strict_types=1);

namespace {{ namespace }};

{{ imports_block }}
final class {{ class_name }}
{
    public static function fromArray(array $data): {{ entity_name }}
    {
        return new {{ entity_name }}(
{% for field in fields %}
            {{ field.from_array_line }},
{% endfor %}
        );
    }

    public static function toArray({{ entity_name }} $entity): array
    {
        return [
{% for field in fields %}
            '{{ field.raw_name }}' => {{ field.to_array_line }},
{% endfor %}
        ];
    }
}
