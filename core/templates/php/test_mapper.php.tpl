<?php

declare(strict_types=1);

namespace {{ namespace }};

use PHPUnit\Framework\TestCase;
{{ imports_block }}
final class {{ class_name }}Test extends TestCase
{
    public function test_can_map_from_array(): void
    {
        $data = [
{% for field in fields %}
            '{{ field.raw_name }}' => {{ field.sample_raw_value }},
{% endfor %}
        ];

        $entity = {{ class_name }}::fromArray($data);

        $this->assertInstanceOf({{ entity_name }}::class, $entity);
    }

    public function test_can_map_to_array(): void
    {
        $entity = new {{ entity_name }}(
{% for field in fields %}
            {{ field.sample_value }},
{% endfor %}
        );

        $data = {{ class_name }}::toArray($entity);

{% for field in fields %}
        $this->assertEquals({{ field.sample_raw_value }}, $data['{{ field.raw_name }}']);
{% endfor %}
    }
}
