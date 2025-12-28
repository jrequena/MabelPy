<?php
declare(strict_types=1);

namespace {{ namespace }}\Enum;

final enum {{ enum_name }}: string
{
{% for value in values %}
    case {{ case }} = '{{ value }}';
{% endfor %}
}
