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

