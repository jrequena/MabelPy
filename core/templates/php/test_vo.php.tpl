<?php

declare(strict_types=1);

namespace {{ namespace }};

use {{ base_test_namespace }}\TestCase;
use {{ vo_import }};

final class {{ class_name }}Test extends TestCase
{
    public function test_can_be_instantiated(): void
    {
        $vo = new {{ class_name }}({{ sample_value }});
        $this->assertInstanceOf({{ class_name }}::class, $vo);
    }

    public function test_can_be_converted_to_string(): void
    {
        $vo = new {{ class_name }}({{ sample_value }});
        $this->assertEquals((string) {{ sample_value }}, (string) $vo);
    }
}
