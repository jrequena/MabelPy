import pytest
from core.contract.validator import ContractValidator
from core.generator.php_enum_generator import PhpEnumGenerator
from core.generator.php_dto_generator import PhpDtoGenerator


def test_validator_rejects_unknown_enum_reference():
    contract = {
        "entity": {"name": "X"},
        "fields": [
            {"name": "status", "type": "enum", "enum": "NotExists"}
        ],
        "enums": {}
    }

    validator = ContractValidator()
    with pytest.raises(ValueError):
        validator.validate(contract)


def test_validator_rejects_bad_enum_structure():
    contract = {
        "entity": {"name": "X"},
        "fields": [],
        "enums": {"Bad": "not-a-mapping"}
    }

    validator = ContractValidator()
    with pytest.raises(ValueError):
        validator.validate(contract)


def test_enum_generator_requires_non_empty_values(tmp_path):
    enum_def = {"type": "string", "values": []}
    gen = PhpEnumGenerator({"namespace": "App"})
    with pytest.raises(ValueError):
        gen.generate("EmptyEnum", enum_def, tmp_path.as_posix())


def test_dto_generator_rejects_unknown_enum_in_normalize():
    dto_gen = PhpDtoGenerator({"namespace": "App"})
    fields = [{"name": "status", "type": "enum", "enum": "X"}]

    with pytest.raises(ValueError):
        dto_gen.normalize_fields(fields, "App", enums={})
