<?php

declare(strict_types=1);

namespace {{ namespace }};

final readonly class {{ class_name }}
{
    public function __construct(
{% for promoted_param in promoted_params %}
        public {{ promoted_param }},
{% endfor %}
    ) {
    }
}
