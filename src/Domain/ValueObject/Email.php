<?php

declare(strict_types=1);

namespace App\Domain\ValueObject;

readonly class Email
{
    public function __construct(
        public string $value
    ) {
        if (!filter_var($value, FILTER_VALIDATE_EMAIL)) {
            throw new \InvalidArgumentException("Invalid email format");
        }
    }

    public function __toString(): string
    {
        return (string) $this->value;
    }
}
