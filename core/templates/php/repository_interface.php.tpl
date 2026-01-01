<?php

declare(strict_types=1);

namespace {{ namespace }};

use {{ entity_import }};

interface {{ class_name }}
{
    public function save({{ entity_name }} $entity): void;
    public function findById(int $id): ?{{ entity_name }};
    public function findAll(): array;
    public function delete(int $id): void;
}
