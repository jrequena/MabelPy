<?php

declare(strict_types=1);

namespace {{ namespace }};

{% for import in imports %}
use {{ import }};
{% endfor %}
use {{ base_test_namespace }}\TestCase;
use Illuminate\Foundation\Testing\RefreshDatabase;

final class {{ class_name }}Test extends TestCase
{
    use RefreshDatabase;

    private {{ class_name }} $repository;

    protected function setUp(): void
    {
        parent::setUp();
        $this->repository = app({{ class_name }}::class);
    }

    public function test_can_save_and_find_entity(): void
    {
        // 1. Create domain entity
        $entity = new {{ entity_name }}(
{% for field in fields %}
{% if not field.is_relation %}
            {{ field.sample_value }},
{% else %}
            null, // Relation: {{ field.raw_name }}
{% endif %}
{% endfor %}
        );

        // 2. Save via repository
        $this->repository->save($entity);

        // 3. Find and verify
        $found = $this->repository->findById($entity->getId());

        $this->assertNotNull($found);
        $this->assertTrue($entity->getId()->equals($found->getId()));
    }

    public function test_can_delete_entity(): void
    {
        $entity = new {{ entity_name }}(
{% for field in fields %}
{% if not field.is_relation %}
            {{ field.sample_value }},
{% else %}
            null,
{% endif %}
{% endfor %}
        );

        $this->repository->save($entity);
        $this->repository->delete($entity->getId());

        $found = $this->repository->findById($entity->getId());
        $this->assertNull($found);
    }
}
