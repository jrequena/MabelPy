# Mabel (Modular Automation Builder Enhanced with Learning)

Mabel is a Python-based code generation system that transforms declarative YAML contracts into production-ready PHP code following **Clean Architecture** principles. It is designed to bridge the gap between architectural design and implementation, ensuring that your code strictly adheres to your domain model.

## 🚀 Key Features

- **Strict Validation**: Formal schema validation for YAML contracts, including type checking for default values and enum members.
- **Clean Architecture**: Automatically generates Domain (Entities, Enums, VOs), Application (Use Cases), and Infrastructure (Mappers, Eloquent) layers.
- **PHP 8.2+ Optimized**: Full support for modern PHP features:
  - `readonly` properties for immutable DTOs and Entities.
  - Native PHP Enums.
  - Strict type hints (including nullable relationships like `?User`).
- **Advanced Mappers**: Smart Infrastructure mappers that handle:
  - Complex relationships (`belongs_to`, `has_one`, `has_many`) with automatic mapper nesting.
  - Robust `DateTimeImmutable` transformations with timezone support (ATOM format).
  - Collection mapping using `array_map` with type safety.
- **Automated Testing**: Generates complete PHPUnit test suites, now including namespaced tests by entity to avoid collisions.
- **CI/CD Ready**: Integrated with GitHub Actions, Ruff (Python linter), and PHP-CS-Fixer (PSR-12).

## 📁 Generated Structure

```text
src/
├── Domain/
│   ├── Entity/          # Immutable Entities (DTO style)
│   ├── Enum/            # Native PHP Enums
│   ├── Repository/      # Domain Repository Interfaces
│   ├── UseCase/         # Application Logic & Request/Response DTOs
│   └── ValueObject/     # Domain VOs with validation
└── Infrastructure/
    ├── Mapper/          # Entity <-> Array mappers with relationship support
    └── Persistence/
        └── Eloquent/    # Laravel Eloquent Models & Repositories
```

## 🛠️ Usage

### Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Commands

**1. Generate Code & Documentation**
```bash
# Generate everything from a contract
python3 mabel.py generate contracts/UserMVP.yaml
```

**2. Format Generated Code**
```bash
# Run PHP-CS-Fixer on the 'src' directory (requires PHP)
python3 mabel.py format
```

**3. Run Tests**
```bash
# Python Tests (Validator, Parser & Generators)
PYTHONPATH=. python3 -m pytest tests/python

# PHP Tests (Generated Code artifacts)
vendor/bin/phpunit
```

## 📋 MVP Status

Mabel has successfully reached **Phase 4** of its development. Current focus is on:
- [x] Formal Contract Schema Validation.
- [x] Robust Relationship Mapping (Infrastructure Layer).
- [x] PHP 8.2 Type Safety & Nullability fixes.
- [x] Automated Namespaced Test Generation.

---
*Mabel is a motor for building modules governed by contracts, using specialized agents and clean architecture.*
