# {{ class_name }}

{{ description }}

**Repository**: `{{ repository_name }}`

## Input

| Field | Type | Required |
|-------|------|----------|
{% for field in request_fields %}
| {{ field.name }} | {{ field.type }} | {{ field.required }} |
{% endfor %}

## Output

| Field | Type |
|-------|------|
{% for field in response_fields %}
| {{ field.name }} | {{ field.type }} |
{% endfor %}
