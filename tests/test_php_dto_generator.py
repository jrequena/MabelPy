from pathlib import Path
from core.generator.php_dto_generator import PhpDtoGenerator
from core.contract.parser import ContractParser
from core.contract.validator import ContractValidator


def test_php_dto_generator_snapshot(tmp_path):
    contract_path = Path("contracts/User.yaml")

    contract = ContractParser().parse(contract_path)
    ContractValidator().validate(contract)

    config = {
        "namespace": "App",
        "output_dir": tmp_path.as_posix(),
        "dto": {
            "readonly": True,
            "validations": True,
        },
    }

    generator = PhpDtoGenerator(config)
    output_file = generator.generate(contract, tmp_path)

    generated = output_file.read_text()
    snapshot = Path("tests/snapshots/UserDto.php").read_text()

    assert generated == snapshot
