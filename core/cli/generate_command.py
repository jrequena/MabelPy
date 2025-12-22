from core.contract.parser import ContractParser
from core.contract.validator import ContractValidator
from core.generator.php_dto_generator import PhpDtoGenerator

class GenerateCommand:
    def execute(self, args):
        if not args:
            print("Usage: generate <contract.yaml>")
            return

        contract_path = args[0]

        print(f"Generating from contract: {contract_path}")

        # 1️⃣ Parse contract
        contract = ContractParser().parse(contract_path)

        # 2️⃣ Validate contract
        ContractValidator().validate(contract)

        print("Contract is valid")

        # 3️⃣ Generate PHP DTO
        generator = PhpDtoGenerator()
        output_file = generator.generate(contract, "generated")

        print(f"DTO generated: {output_file}")
