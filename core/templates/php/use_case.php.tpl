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
        // TODO: Implement business logic
        return new {{ response_class }}();
    }
}
