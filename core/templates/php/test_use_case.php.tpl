<?php

declare(strict_types=1);

namespace {{ namespace }};

{% for import in imports %}
use {{ import }};
{% endfor %}

use {{ base_test_namespace }}\TestCase;
use {{ base_test_namespace }}\RefreshDatabase;

final class {{ class_name }}Test extends TestCase
{
    use RefreshDatabase;

    public function test_can_be_instantiated(): void
    {
        $useCase = $this->app({{ class_name }}::class);
        $this->assertInstanceOf({{ class_name }}::class, $useCase);
    }
}
