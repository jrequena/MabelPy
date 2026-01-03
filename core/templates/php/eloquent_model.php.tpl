<?php

declare(strict_types=1);

namespace {{ namespace }};

use Illuminate\Database\Eloquent\Model;
{% for import in imports %}
use {{ import }};
{% endfor %}

final class {{ class_name }} extends Model
{
    protected $table = '{{ table_name }}';

    protected $fillable = [
{% for field in fillable %}
        '{{ field }}',
{% endfor %}
    ];

{% for rel in relationships %}
    public function {{ rel.name }}(): {{ rel.return_type }}
    {
        return $this->{{ rel.method }}({{ rel.target_class }});
    }

{% endfor %}
}
