<?php
declare(strict_types=1);

namespace {{ namespace }}\Dto;


{{ imports_block }}

final class {{ class_name }}
{
    public function __construct(
{% for promoted_param in promoted_params %}
        {{ promoted_param }},
{% endfor %}
    ) {
{% for validation in validations %}
        {{ validation }}
{% endfor %}
    }
}