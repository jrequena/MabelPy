<?php

declare(strict_types=1);

namespace {{ namespace }};

{{ readonly }}class {{ class_name }}
{
    public function __construct(
        public {{ type }} $value
    ) {
        {{ validations }}
    }

    public function __toString(): string
    {
        return (string) $this->value;
    }
}
