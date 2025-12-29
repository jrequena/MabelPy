<?php

declare(strict_types=1);

namespace {{ namespace }};

enum {{ class_name }}: string
{
{% for item in values %}
    case {{ item.case }} = '{{ item.value }}';
{% endfor %}
}
