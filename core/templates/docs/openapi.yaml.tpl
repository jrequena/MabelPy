openapi: 3.0.0
info:
  title: {{ project_name }} API
  version: {{ version | default("1.0.0") }}
paths:
{% for uc_name, uc in use_cases.items() %}
  /api/{{ uc.entity_path }}/{{ uc.name_path }}:
    post:
      summary: {{ uc.description }}
      operationId: {{ uc_name }}
      tags:
        - {{ uc.entity }}
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/{{ uc_name }}Request'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/{{ uc_name }}Response'
{% endfor %}

components:
  schemas:
{% for uc_name, uc in use_cases.items() %}
    {{ uc_name }}Request:
      type: object
      properties:
{% for field, type in uc.input.items() %}
        {{ field | replace('?', '') }}:
          {{ type | to_openapi_type }}
{% endfor %}
{% if uc.is_list %}
        page:
          type: integer
          default: 1
        per_page:
          type: integer
          default: 15
{% endif %}
    {{ uc_name }}Response:
      type: object
      properties:
{% if uc.is_list %}
        items:
          type: array
          items:
            {{ uc.output | to_openapi_type }}
        meta:
          type: object
          properties:
            total: { type: integer }
            per_page: { type: integer }
            current_page: { type: integer }
            last_page: { type: integer }
{% else %}
        data:
          {{ uc.output | to_openapi_type }}
{% endif %}
{% endfor %}
{% for entity_name, entity in entities.items() %}
    {{ entity_name }}:
      type: object
      properties:
{% for field, type in entity.items() %}
        {{ field }}:
          {{ type | to_openapi_type }}
{% endfor %}
{% endfor %}
