<?php

declare(strict_types=1);

namespace {{ namespace }};

{% for import in imports %}
use {{ import }};
{% endfor %}

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
