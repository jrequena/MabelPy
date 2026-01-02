<?php

declare(strict_types=1);

namespace {{ namespace }};

{% for import in imports %}
use {{ import }};
{% endfor %}
use {{ base_test_namespace }}\TestCase;
use {{ base_test_namespace }}\RefreshDatabase;

final class {{ class_name }}Test extends TestCase
{
    use RefreshDatabase;

    private {{ class_name }} $repository;

    protected function setUp(): void
    {
        parent::setUp();
        $this->repository = $this->app({{ class_name }}::class);
    }

    public function test_can_save_and_find_entity(): void
    {
        // 1. Create domain entity
        $entity = new {{ entity_name }}(
{% for field in fields %}
            {{ field.sample_value }},
{% endfor %}
        );

        // 2. Save via repository
        $this->repository->save($entity);

        // 3. Find and verify
        $found = $this->repository->findById($entity->id);

        $this->assertNotNull($found);
        $this->assertEquals($entity->id, $found->id);
    }

    public function test_can_delete_entity(): void
    {
        $entity = new {{ entity_name }}(
{% for field in fields %}
            {{ field.sample_value }},
{% endfor %}
        );

        $this->repository->save($entity);
        $this->repository->delete($entity->id);

        $found = $this->repository->findById($entity->id);
        $this->assertNull($found);
    }
}
