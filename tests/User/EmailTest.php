<?php

declare(strict_types=1);

namespace App\Tests;

use PHPUnit\Framework\TestCase;
use App\Domain\ValueObject\Email;

final class EmailTest extends TestCase
{
    public function test_can_be_instantiated(): void
    {
        $vo = new Email('test@example.com');
        $this->assertInstanceOf(Email::class, $vo);
    }

    public function test_can_be_converted_to_string(): void
    {
        $vo = new Email('test@example.com');
        $this->assertEquals((string) 'test@example.com', (string) $vo);
    }
}
