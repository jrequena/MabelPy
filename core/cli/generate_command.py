from pathlib import Path
from core.generator.php_dto_generator import PhpDtoGenerator
from core.generator.php_enum_generator import PhpEnumGenerator
from core.generator.php_vo_generator import PhpValueObjectGenerator
from core.generator.php_repository_generator import PhpRepositoryGenerator
from core.generator.php_usecase_generator import PhpUseCaseGenerator
from core.generator.php_mapper_generator import PhpMapperGenerator
from core.generator.php_test_generator import PhpTestGenerator
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
            for field in contract.get("fields", []):
                vo_name = field["type"]
                if vo_name in auto_types and vo_name not in generated_vos:
                    vo_gen.generate(vo_name, vo_name, output_dir)
                    generated_vos.add(vo_name)

            # 3. Entities (DTOs)
            PhpDtoGenerator(self.config).generate(contract, output_dir)
            
            # 4. Repository Interface
            PhpRepositoryGenerator(self.config).generate(contract, output_dir)
            
            # 5. Use Cases
            PhpUseCaseGenerator(self.config).generate(contract, output_dir)
            
            # 6. Mappers (Infrastructure)
            PhpMapperGenerator(self.config).generate(contract, output_dir)
            
            # 7. Tests
            if self.config.get("generators.tests.enabled", True):
                PhpTestGenerator(self.config).generate(contract, output_dir)
            
            print(f"✓ Generation complete for {contract_path}")
            print(f"  Output directory: {output_dir}")
            
        except Exception as e:
            print(f"✗ Generation failed: {e}")
            import traceback
            traceback.print_exc()
