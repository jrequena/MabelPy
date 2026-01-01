<?php

declare(strict_types=1);

namespace {{ namespace }};

use {{ interface_import }};
use {{ model_import }};
use {{ entity_import }};
use {{ mapper_import }};
{% for import in imports %}
use {{ import }};
{% endfor %}

final class {{ class_name }} implements {{ interface_name }}
{
    public function __construct(
        private readonly {{ model_name }} $model
    ) {
    }

    public function findById(int $id): ?{{ entity_name }}
    {
        $eloquent = $this->model
{% if relationships %}
            ->with([
{% for rel in relationships %}
                '{{ rel.name }}',
{% endfor %}
            ])
{% endif %}
            ->find($id);

        if (!$eloquent) {
            return null;
        }

        return {{ mapper_name }}::fromArray($eloquent->toArray());
    }

    public function findAll(): array
    {
        return $this->model
{% if relationships %}
            ->with([
{% for rel in relationships %}
                '{{ rel.name }}',
{% endfor %}
            ])
{% endif %}
            ->all()
            ->map(fn({{ model_name }} $item) => {{ mapper_name }}::fromArray($item->toArray()))
            ->toArray();
    }

    public function save({{ entity_name }} $entity): void
    {
        $data = {{ mapper_name }}::toArray($entity);
        
        DB::transaction(function () use ($data) {
            $mainData = $data;
            {% for rel in relationships %}
            unset($mainData['{{ rel.name }}']);
            {% if rel.type == 'belongs_to' %}
            if (isset($data['{{ rel.name }}']['id'])) {
                $mainData['{{ rel.name }}_id'] = $data['{{ rel.name }}']['id'];
            }
            {% endif %}
            {% endfor %}

            $eloquent = $this->model->updateOrCreate(
                ['id' => $data['id'] ?? null],
                $mainData
            );

            {% for rel in relationships %}
            {% if rel.type == 'has_many' %}
            if (isset($data['{{ rel.name }}'])) {
                foreach ($data['{{ rel.name }}'] as $itemData) {
                    $eloquent->{{ rel.name }}()->updateOrCreate(
                        ['id' => $itemData['id'] ?? null],
                        $itemData
                    );
                }
            }
            {% elif rel.type == 'has_one' %}
            if (isset($data['{{ rel.name }}'])) {
                $eloquent->{{ rel.name }}()->updateOrCreate(
                    ['id' => $data['{{ rel.name }}']['id'] ?? null],
                    $data['{{ rel.name }}']
                );
            }
            {% endif %}
            {% endfor %}
        });
    }

    public function delete(int $id): void
    {
        $this->model->destroy($id);
    }
}
