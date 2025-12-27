from core.generator.php_dto_generator import PhpDtoGenerator
from core.generator.php_enum_generator import PhpEnumGenerator
from core.contract.parser import ContractParser
from core.contract.validator import ContractValidator


class GenerateCommand:
    def __init__(self, config: dict):
        self.config = config

    def execute(self, args: list):
        contract_path = args[0]

        contract = ContractParser().parse(contract_path)
        ContractValidator().validate(contract)

        output_dir = self.config.get("output_dir", "generated")

        # Generate enums first
        if "enums" in contract:
            enum_gen = PhpEnumGenerator(self.config)
            for name, enum_def in contract["enums"].items():
                enum_gen.generate(name, enum_def, output_dir)

        # Then DTOs
        generator = PhpDtoGenerator(self.config)
        generator.generate(contract, output_dir)
