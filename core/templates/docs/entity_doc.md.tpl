# Entity: {{ entity_name }}

{{ description }}

## Fields

| Name | Type | Nullable | Validation | Description |
|------|------|----------|------------|-------------|
{% for field in fields %}
| `{{ field.name }}` | `{{ field.type }}` | {{ field.nullable }} | {{ field.validation }} | {{ field.description }} |
{% endfor %}

## Domain Rules
- Managed as a strictly typed DTO.
- Immutable by default.
- Validation performed at constructor level.
