<?php

declare(strict_types=1);

namespace {{ namespace }};

{{ imports_block }}
final class {{ class_name }}
{
    public function __construct(
        private readonly {{ repository_name }} $repository
    ) {
    }

    public function execute({{ request_class }} $request): {{ response_class }}
    {
{% for rule in business_rules %}
        {{ rule }}
{% endfor %}

        // TODO: Implement actual execution and persistence
        return new {{ response_class }}();
    }
}
