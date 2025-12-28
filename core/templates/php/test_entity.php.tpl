<?php

declare(strict_types=1);

namespace {{ namespace }};

use PHPUnit\Framework\TestCase;
{{ imports_block }}

final class {{ class_name }}Test extends TestCase
{
    public function test_can_be_instantiated(): void
    {
        $entity = new {{ class_name }}(
{% for field in fields %}
            {{ field.sample_value }},
{% endfor %}
        );

        $this->assertInstanceOf({{ class_name }}::class, $entity);
    }
}
