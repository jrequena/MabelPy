<?php

declare(strict_types=1);

namespace {{ namespace }};

{{ readonly }}class {{ class_name }} implements \JsonSerializable
{
    public function __construct(
        public {{ type }} $value
    ) {
{% if validations %}
        {{ validations|indent(8) }}
{% endif %}
    }

    public static function fromValue({{ type }} $value): self
    {
        return new self($value);
    }

    public function equals(self $other): bool
    {
        return $this->value === $other->value;
    }

    public function jsonSerialize(): {{ type }}
    {
        return $this->value;
    }

    public function __toString(): string
    {
        return (string) $this->value;
    }
}
