<?php

declare(strict_types=1);

namespace {{ namespace }};

enum {{ class_name }}: string
{
{% for value in values %}
    case {{ case }} = '{{ value }}';
{% endfor %}
}
