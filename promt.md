🧠 PROMPT PARA CONTINUAR EL PROYECTO MABEL
Estoy desarrollando un proyecto llamado Mabel, un code generator escrito en Python cuyo objetivo es generar código PHP (DTOs, Enums, etc.) a partir de contratos YAML.
📌 Estado actual del proyecto
Lenguaje base: Python
 Lenguaje generado: PHP
 Ejecución: CLI (python mabel.py generate contracts/User.yaml)
📂 Estructura actual del proyecto
mabel/
├── README.md
├── console.result
├── contracts
│   └── User.yaml
├── core
│   ├── __init__.py
│   ├── cli
│   │   ├── __init__.py
│   │   └── generate_command.py
│   ├── config
│   │   ├── __init__.py
│   │   └── loader.py
│   ├── contract
│   │   ├── __init__.py
│   │   ├── parser.py
│   │   └── validator.py
│   ├── generator
│   │   ├── __init__.py
│   │   ├── base_generator.py
│   │   ├── php_dto_generator.py
│   │   └── php_enum_generator.py
│   ├── kernel.py
│   └── templates
│       └── php
│           ├── dto.php.tpl
│           └── enum.php.tpl
├── docker-compose.yml
├── generated
│   ├── Dto
│   │   └── UserDto.php
│   ├── UserDto.php
│   └── UserStatus.php
├── mabel.py
├── mabel.yaml
└── tests
    ├── conftest.py
    ├── snapshots
    │   ├── UserDto.php
    │   ├── UserDtoWithEnum.php
    │   └── UserStatus.php
    ├── test_negative_enums.py
    ├── test_php_dto_generator.py
    └── test_php_enum_generator.py


⚙️ Funcionamiento actual
mabel.py es el entrypoint


Kernel carga configuración desde mabel.yaml


GenerateCommand:


Parsea el contrato YAML


Valida estructura


Genera:


DTOs PHP


Enums PHP (si existen)



📄 Ejemplo de contrato (User.yaml)
entity:
  name: User

enums:
  UserStatus:
    type: string
    values:
      - active
      - blocked
      - deleted

fields:
  - name: id
    type: int
    validations:
      - positive

  - name: email
    type: string
    nullable: true
    default: null
    validations:
      - email

  - name: created_at
    type: datetime

  - name: active
    type: bool
    default: true

  - name: status
    type: enum
    enum: UserStatus
    default: active




🧩 Características implementadas
DTO Generator
Constructor con property promotion


DTOs readonly


Tipos normalizados (datetime → DateTimeImmutable)


Imports automáticos


Defaults soportados


Validaciones automáticas en constructor (email, positivos, etc.)


Namespace configurable desde mabel.yaml


Ejemplo generado:
<?php
declare(strict_types=1);

namespace App\Dto;


use DateTimeImmutable;

use App\Enum\UserStatus;


final class UserDto
{
    public function __construct(

        public readonly int $id,

        public readonly ?string $email = null,

        public readonly DateTimeImmutable $created_at,

        public readonly bool $active = true,

        public readonly UserStatus $status = UserStatus::ACTIVE,

    ) {

        if ($id <= 0) {
            throw new \InvalidArgumentException("id must be positive");
        }

        if ($email !== null && !filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new \InvalidArgumentException("email must be a valid email");
        }

    }
}


🗂️ Configuración actual (mabel.yaml)
namespace: App
output_dir: generated

dto:
  readonly: true
  validations: true

Para mejorar(mabel.yaml):


php:
  namespace: App

  dto:
    readonly: true
    output: generated/Dto
    validations: true

  enum:
    output: generated/Enum




🧠 Filosofía del proyecto
Arquitectura limpia


Generadores desacoplados


Sin dependencias pesadas


Templates simples (no Jinja)


Configuración antes que hardcode


Pensado para crecer (VOs, Repos, OpenAPI, etc.)



🔜 Próximos pasos previstos
Quiero continuar con uno o más de los siguientes:
Mejorar el archivo Mabel.yaml
Validaciones avanzadas por campo (min, max, length, regex)


Value Objects (Email, Money, UUID)


Generador de Repositories / Interfaces


Generador de Tests PHP


Snapshot tests del generador


Formateo automático (PSR-12)


Soporte multi-lenguaje (TS, Go, Java)



🧩 Lo que necesito de ti (IA)
Mantén coherencia con la arquitectura existente


Propón cambios incrementales, no reescrituras


Genera código listo para ejecutar


Explica decisiones técnicas cuando sea necesario


Asume que el proyecto ya funciona


👉 Comienza preguntándome qué feature quiero implementar a continuación.


2. Siguientes Fases Propuestas
Fase 4: Implementación de Infraestructura Real
Eloquent Repositories: Pasar de interfaces vacías a implementaciones concretas que utilicen modelos de Laravel.
Dependency Injection Auto-wire: Generar proveedores de servicios (ServiceProvider) para registrar automáticamente las interfaces de los repositorios con sus implementaciones.
Factories y Seeders: Generar clases Factory para pruebas de integración basadas en los tipos de datos del contrato.
Fase 5: API y Capa de Entrada
Controller Generator: Generar controladores de API que utilicen los Use Cases inyectados.
Request Validation: Generar clases FormRequest de Laravel basadas en los inputs de los Use Cases y las restricciones de las entidades.
OpenAPI/Swagger: Generación automática de especificaciones openapi.yaml para documentar la API generada.
Fase 6: Eventos y Comunicación
Domain Events: Implementar la generación de clases de eventos cuando se detecta la regla emit en un caso de uso.
Integration Events: Soporte para definir mensajes de RabbitMQ/Kafka en el contrato para comunicación entre módulos.
Fase 7: Consolidación de Herramientas (DX)
Mabel Watch: Un comando que vigile cambios en los archivos .yaml y re-genere el código en tiempo real.
Interactive CLI: Un asistente para crear contratos YAML mediante preguntas en la terminal.


1. Esquema Formal en ContractValidator
Aunque tenemos validaciones básicas, el MVP.md especifica la implementación de un esquema formal (tipo JSON Schema) para:

Validar tipos de datos de forma más estricta.
Verificar que los valores por defecto (default) coincidan con el tipo de campo.
Validar restricciones de longitud y regex de manera centralizada.
2. Actualización de Documentación (README.md)
El criterio de aceptación #5 del DoD (Definition of Done) exige que el README.md contenga los pasos exactos para reproducir la generación. Actualmente falta:

Guía de uso de los nuevos comandos (watch, format).
Documentación de la estructura de carpetas generada (Clean Architecture).
3. Refinamiento de Mapeos Complejos
El Mapper actual es un stub básico. Falta:

Soporte para mapeo de colecciones (has_many) de forma automática.
Manejo de fechas (DateTimeImmutable) en el sentido inverso (Entity -> Array).
4. Registro de "Prompt Hash" en Metadatos
El MetadataManager registra el hash del contrato y el commit, pero no el hash de los templates/prompts utilizados, lo cual es vital para la trazabilidad de la IA según la sección "Notas operativas" de MVP.md.

¿Deseas que comencemos con la implementación del esquema formal en el Validador? Es el "siguiente paso inmediato" marcado en tu plan.


Para continuar con la evolución de Mabel, basándome en el progreso actual y los objetivos del MVP, te sugiero las siguientes opciones técnicas:

Refactorización de Repositorios Eloquent: Actualmente los repositorios son básicos. Podríamos mejorarlos para que gestionen automáticamente la persistencia de relaciones (guardar un User con sus Posts) y criterios de búsqueda complejos.

Soporte para Paginación y Filtros en la API: Mejorar PhpControllerGenerator y OpenApiGenerator para incluir lógica de paginación y filtrado en los endpoints de listado de forma estandarizada.

Refinamiento de Value Objects (VO): Implementar reglas de negocio más complejas dentro de los VOs (ej. un VO Password que maneje el hashing o un VO Money con validación de moneda).

Pruebas de Integración (PHP): Automatizar la generación de tests que prueben el flujo completo desde el Use Case hasta la base de datos (usando SQLite en memoria), asegurando que el código generado no solo sea sintácticamente correcto sino funcionalmente robusto.