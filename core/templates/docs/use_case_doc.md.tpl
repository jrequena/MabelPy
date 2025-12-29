# Use Case: {{ class_name }}

## Description
{{ description }}

## Request (DTO)
| Field | Type | Required |
|-------|------|----------|
{% for field in request_fields %}
| `{{ field.name }}` | `{{ field.type }}` | {{ field.required }} |
{% endfor %}

## Response (DTO)
| Field | Type |
|-------|------|
{% for field in response_fields %}
| `{{ field.name }}` | `{{ field.type }}` |
{% endfor %}

## Flow
1. Receive Request DTO.
2. Validate business rules.
3. Interact with `{{ repository_name }}`.
4. Return Response DTO.
