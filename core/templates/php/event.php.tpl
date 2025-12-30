<?php

declare(strict_types=1);

namespace {{ namespace }};

use Illuminate\Foundation\Events\Dispatchable;
use Illuminate\Queue\SerializesModels;

final class {{ class_name }}
{
    use Dispatchable, SerializesModels;

    public function __construct(
        {% if entity_class %}
        public readonly {{ entity_class }} $entity
        {% endif %}
    ) {
    }
}
