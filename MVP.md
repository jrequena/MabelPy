Mabel — MVP técnico
====================

Objetivo
--------
Definir y entregar un MVP reproducible que demuestre el flujo: contrato (YAML) → validación → generación determinista de artefactos PHP (DTO, Enum, Entity, Repository stub, Mapper stub) + pruebas automáticas y pipeline CI.

Alcance (entregables)
---------------------
- `contracts/UserMVP.yaml`: contrato oficial de ejemplo.
- `MVP.md`: este documento (alcance y criterios).
- Generadores:
  - DTO
  - Enum
  - Entity
  - Repository (stub, Eloquent style)
  - Mapper (Entity <-> DTO stub)
- Validaciones:
  - `ContractValidator` con schema formal que verifica tipos, enums, referencias y constraints básicas (min/max/length/regex).
- Tests:
  - Pruebas unitarias y de integración con `pytest` y snapshots (`tests/snapshots`).
- CI:
  - Pipeline para linters (Python), tests y formateo PHP (php-cs-fixer) sobre artefactos generados.
- Documentación mínima:
  - `MVP.md` y actualización de `README.md` con cómo ejecutar el demo.

Criterios de aceptación (Definition of Done)
-------------------------------------------
1. `contracts/UserMVP.yaml` valida correctamente con `ContractValidator`.
2. Generación desde dicho YAML produce archivos PHP que coinciden con los snapshots almacenados en `tests/snapshots`.
3. `pytest` pasa en local con cobertura razonable de los generadores.
4. Un pipeline CI (GitHub Actions) ejecuta linters, `pytest` y aplica `php-cs-fixer` a los artefactos generados sin errores.
5. Documentación con pasos para reproducir la generación está en el README.

Estimaciones y prioridad
------------------------
- Sprint 1 (3-5 días): finalizar `MVP.md`, `contracts/UserMVP.yaml`, implementar schema básico y tests de validación (tareas 1+2).
- Sprint 2 (4-6 días): implementar generadores DTO/Enum/Entity y snapshots (tarea 3).
- Sprint 3 (3 días): repos/mapper stubs + tests (tarea 4).
- Sprint 4 (2-3 días): CI + linter + docs (tarea 6+9).

Notas operativas
----------------
- Mantener los prompts y plantillas de generación versionados (carpeta `prompts/` y `templates/`).
- Metadata: cada generación debería registrar `commit`, `timestamp` y `prompt-hash` en un archivo de metadatos junto al artefacto.

Siguiente paso inmediato
------------------------
- Implementar y validar el schema formal en `core/contract/validator.py` y añadir pruebas unitarias.

Contacto
--------
- Si estás de acuerdo, empiezo por implementar `ContractValidator` y los tests de validación.
