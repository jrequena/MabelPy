from pathlib import Path
from core.metadata.manager import MetadataManager
from core.generator.php_dto_generator import PhpDtoGenerator
from core.generator.php_enum_generator import PhpEnumGenerator
from core.generator.php_vo_generator import PhpValueObjectGenerator
from core.generator.php_repository_generator import PhpRepositoryGenerator
from core.generator.php_usecase_generator import PhpUseCaseGenerator
from core.generator.php_mapper_generator import PhpMapperGenerator
from core.generator.php_test_generator import PhpTestGenerator
from core.generator.php_doc_generator import PhpDocGenerator
from core.generator.php_migration_generator import PhpMigrationGenerator
from core.generator.php_eloquent_model_generator import PhpEloquentModelGenerator
from core.generator.php_eloquent_repository_generator import PhpEloquentRepositoryGenerator
from core.generator.php_service_provider_generator import PhpServiceProviderGenerator
from core.generator.php_factory_generator import PhpFactoryGenerator
from core.generator.php_seeder_generator import PhpSeederGenerator
from core.contract.parser import ContractParser
from core.contract.validator import ContractValidator
from core.config import MabelConfig


class GenerateCommand:
    def __init__(self, config: MabelConfig):
        self.config = config

    def execute(self, args: list):
        if not args:
            print("Error: Contract path required")
            return

        contract_path = args[0]

        try:
            contract = ContractParser().parse(contract_path)
            ContractValidator().validate(contract)

            # Unified format normalization
            if "entities" not in contract and "entity" in contract:
                fields_list = contract["fields"]
                field_map = {}
                for f in fields_list:
                    fname = f["name"]
                    fd = dict(f)
                    fd.pop("name", None)
                    field_map[fname] = fd
                contract["entities"] = {contract["entity"]["name"]: field_map}

            output_dir = Path(self.config.get("paths.source_root", "src")).absolute()

            # 1. Enums
            if "enums" in contract:
                enum_gen = PhpEnumGenerator(self.config)
                for name, enum_def in contract["enums"].items():
                    enum_gen.generate(name, enum_def, output_dir)

            # 2. Value Objects
            vo_gen = PhpValueObjectGenerator(self.config)
            auto_types = self.config.get("generators.value_objects.auto_types", [])
            generated_vos = set()
            for entity_fields in contract.get("entities", {}).values():
                for field_def in entity_fields.values():
                    vo_name = field_def if isinstance(field_def, str) else field_def.get("type")
                    if vo_name in auto_types and vo_name not in generated_vos:
                        vo_gen.generate(vo_name, vo_name, output_dir)
                        generated_vos.add(vo_name)

            # 3. Entities (DTOs)
            dto_gen = PhpDtoGenerator(self.config)
            for entity_name, fields in contract.get("entities", {}).items():
                entity_contract = {
                    "entity": {"name": entity_name},
                    "fields": self._normalize_fields_to_list(fields),
                    "enums": contract.get("enums", {}),
                    "use_cases": contract.get("use_cases", {})
                }
                dto_gen.generate(entity_contract, output_dir)
            
            # 4. Repository Interface
            repo_gen = PhpRepositoryGenerator(self.config)
            for entity_name, fields in contract.get("entities", {}).items():
                entity_contract = {
                    "entity": {"name": entity_name},
                    "fields": self._normalize_fields_to_list(fields)
                }
                repo_gen.generate(entity_contract, output_dir)
            
            # 5. Use Cases
            PhpUseCaseGenerator(self.config).generate(contract, output_dir)
            
            # 6. Mappers (Infrastructure)
            mapper_gen = PhpMapperGenerator(self.config)
            for entity_name, fields in contract.get("entities", {}).items():
                entity_contract = {
                    "entity": {"name": entity_name},
                    "fields": self._normalize_fields_to_list(fields),
                    "enums": contract.get("enums", {}),
                    "use_cases": contract.get("use_cases", {})
                }
                mapper_gen.generate(entity_contract, output_dir)

            # 7. Eloquent Models & Repositories
            PhpEloquentModelGenerator(self.config).generate(contract, output_dir)
            PhpEloquentRepositoryGenerator(self.config).generate(contract, output_dir)
            PhpServiceProviderGenerator(self.config).generate(contract, output_dir)
            
            # 8. Database (Migrations, Factories, Seeders)
            PhpMigrationGenerator(self.config).generate(contract, output_dir)
            PhpFactoryGenerator(self.config).generate(contract, output_dir)
            PhpSeederGenerator(self.config).generate(contract, output_dir)

            # 9. Tests
            if self.config.get("generators.tests.enabled", True):
                test_gen = PhpTestGenerator(self.config)
                for entity_name, fields in contract.get("entities", {}).items():
                    entity_contract = {
                        "entity": {"name": entity_name},
                        "fields": self._normalize_fields_to_list(fields),
                        "enums": contract.get("enums", {}),
                        "use_cases": contract.get("use_cases", {})
                    }
                    test_gen.generate(entity_contract, output_dir)
            
            # 10. Documentation
            if self.config.get("generators.documentation.enabled", True):
                doc_gen = PhpDocGenerator(self.config)
                for entity_name, fields in contract.get("entities", {}).items():
                    entity_contract = {
                        "entity": {"name": entity_name},
                        "fields": self._normalize_fields_to_list(fields),
                        "enums": contract.get("enums", {}),
                        "use_cases": contract.get("use_cases", {})
                    }
                    doc_gen.generate(entity_contract, output_dir)
            
            # Record metadata
            MetadataManager(output_dir).record_generation(Path(contract_path))

            print(f"✓ Generation complete for {contract_path}")
            print(f"  Output directory: {output_dir}")
            
        except Exception as e:
            print(f"✗ Generation failed: {e}")
            import traceback
            traceback.print_exc()

    def _normalize_fields_to_list(self, fields: dict) -> list:
        normalized = []
        for name, definition in fields.items():
            if isinstance(definition, str):
                normalized.append({"name": name, "type": definition})
            else:
                d = dict(definition)
                d["name"] = name
                normalized.append(d)
        return normalized
