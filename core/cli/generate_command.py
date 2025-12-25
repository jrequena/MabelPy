from core.generator.php_dto_generator import PhpDtoGenerator
from core.contract.parser import ContractParser
from core.contract.validator import ContractValidator


class GenerateCommand:
    def __init__(self, config: dict):
        self.config = config

    def execute(self, args: list):
        contract_path = args[0]

        contract = ContractParser().parse(contract_path)
        ContractValidator().validate(contract)

        generator = PhpDtoGenerator(self.config)
        output_dir = self.config.get("output_dir", "generated")

        generator.generate(contract, output_dir)
