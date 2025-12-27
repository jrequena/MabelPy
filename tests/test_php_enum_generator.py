from pathlib import Path
from core.generator.php_enum_generator import PhpEnumGenerator
from core.generator.php_dto_generator import PhpDtoGenerator
from core.contract.parser import ContractParser
from core.contract.validator import ContractValidator


def test_php_enum_and_dto_generation_snapshot(tmp_path):
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

    enum_generator = PhpEnumGenerator(config)

    # Generate enums
    for name, enum_def in contract.get("enums", {}).items():
        enum_file = enum_generator.generate(name, enum_def, tmp_path.as_posix())
        generated_enum = enum_file.read_text()
        snapshot_enum = Path("tests/snapshots/UserStatus.php").read_text()
        assert generated_enum == snapshot_enum

    # Generate DTO
    dto_generator = PhpDtoGenerator(config)
    dto_file = dto_generator.generate(contract, tmp_path.as_posix())
    generated_dto = dto_file.read_text()
    snapshot_dto = Path("tests/snapshots/UserDtoWithEnum.php").read_text()

    assert generated_dto == snapshot_dto
