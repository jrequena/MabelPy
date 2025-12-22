<?php
declare(strict_types=1);

namespace {{ namespace }}\Dto;

{% for import in imports %}
use {{ import }};
{% endfor %}

final class {{ class_name }}
{
{% for field in fields %}
    public {{ field.type }} ${{ field.name }};
{% endfor %}
}
