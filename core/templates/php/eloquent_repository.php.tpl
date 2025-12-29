<?php

declare(strict_types=1);

namespace {{ namespace }};

use {{ interface_import }};
use {{ model_import }};
{% for import in imports %}
use {{ import }};
{% endfor %}

final class {{ class_name }} implements {{ interface_name }}
{
    public function __construct(
        private readonly {{ model_name }} $model
    ) {
    }

    public function findById(int $id): ?object
    {
        // TODO: Implement mapping from Eloquent to Domain Entity
        return $this->model->find($id);
    }

    public function save(object $entity): void
    {
        // TODO: Implement mapping from Domain Entity to Eloquent
        $this->model->updateOrCreate(
            ['id' => $entity->id ?? null],
            [] // Add mapping logic
        );
    }
}
