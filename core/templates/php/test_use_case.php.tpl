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
        $repository = $this->createMock({{ repository_name }}::class);
        $useCase = new {{ class_name }}($repository);
        
        $this->assertInstanceOf({{ class_name }}::class, $useCase);
    }
}
