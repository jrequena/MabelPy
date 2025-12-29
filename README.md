# Mabel (Modular Automation Builder Enhanced with Learning)

Mabel is a Python-based code generation system that transforms declarative YAML contracts into production-ready PHP code following **Clean Architecture** principles.

## 🚀 Key Features

- **Strict Validation**: Formal schema validation for YAML contracts.
- **Clean Architecture**: Generates Domain, Application, and Infrastructure layers.
- **PHP 8.2+ Support**: Uses modern PHP features like readonly properties and native enums.
- **Automated Testing**: Generates PHPUnit test suites for all generated artifacts.
- **Documentation**: Automatically produces Markdown documentation for Entities and Use Cases.
- **Metadata Tracking**: Records generation history including commit hashes and contract versions.
- **CI/CD Ready**: Includes GitHub Actions workflow and PHP-CS-Fixer support.

## 📁 Generated Structure

```text
src/
├── Domain/
│   ├── Entity/          # Entities (DTO style)
│   ├── Enum/            # PHP Enums
│   ├── Repository/      # Interfaces
│   ├── UseCase/         # Request/Response DTOs and Logic
│   └── ValueObject/     # Domain VOs (Email, Id, etc.)
└── Infrastructure/
    └── Mapper/          # Entity <-> Array mappers
```

## 🛠️ Usage

### Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Commands

**Generate Code & Documentation**
```bash
python3 mabel.py generate contracts/UserMVP.yaml
```

**Format Generated Code (requires PHP)**
```bash
python3 mabel.py format
```

**Run Tests**
```bash
# Python Tests (Validator & Generators)
python3 -m pytest tests/python

# PHP Tests (Generated Code)
vendor/bin/phpunit
```

## 📋 MVP Status

The project has successfully completed Phase 3 of its MVP. It strictly adheres to:
- **PSR-12** Coding Standards.
- **Hexagonal Architecture** (Infrastructure separation).
- **Deterministic Generation** verified by snapshots.

---
*Mabel is a motor for building modules governed by contracts, using specialized agents and clean architecture.*
