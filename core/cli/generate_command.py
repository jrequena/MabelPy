from core.generator.php_dto_generator import PhpDtoGenerator
from core.generator.php_enum_generator import PhpEnumGenerator
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

            # Use source_root from config
            output_dir = self.config.get("paths.source_root", "src")

            # Generate enums first
            if "enums" in contract:
                # Still passing dict to generators for now as they expect dict
                enum_gen = PhpEnumGenerator(self.config.to_dict())
                for name, enum_def in contract["enums"].items():
                    enum_gen.generate(name, enum_def, output_dir)

            # Then DTOs
            generator = PhpDtoGenerator(self.config.to_dict())
            generator.generate(contract, output_dir)
            
            print(f"✓ Generation complete for {contract_path}")
            
        except Exception as e:
            print(f"✗ Generation failed: {e}")
