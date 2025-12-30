<?php

declare(strict_types=1);

namespace {{ namespace }};

{% for import in imports %}
use {{ import }};
{% endfor %}

final class {{ class_name }} extends ServiceProvider
{
    public function register(): void
    {
{% for binding in bindings %}
        $this->app->bind({{ binding.interface_name }}::class, {{ binding.implementation_name }}::class);
{% endfor %}
    }
}
