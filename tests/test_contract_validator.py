import yaml
import pytest
from core.contract.validator import ContractValidator


def load_contract(path: str):
    with open(path) as f:
        return yaml.safe_load(f)


def test_user_mvp_contract_validates():
    contract = load_contract("contracts/UserMVP.yaml")
    ContractValidator().validate(contract)  # should not raise


def test_enum_missing_values_raises():
    bad = {
        "module": {"name": "X", "namespace": "App\\X"},
        "entities": {"A": {"id": "int"}},
        "enums": {"Status": {"type": "string"}}
    }
    with pytest.raises(ValueError, match="must define a non-empty 'values' list"):
        ContractValidator().validate(bad)


def test_undefined_enum_reference_raises():
    bad = {
        "module": {"name": "X", "namespace": "App\\X"},
        "entities": {"User": {"id": "int", "status": "UserStatus"}}
    }
    with pytest.raises(ValueError, match="Unknown type referenced"):
        ContractValidator().validate(bad)


def test_enum_field_without_enum_name_raises():
    bad = {
        "module": {"name": "X", "namespace": "App\\X"},
        "entities": {"User": {"id": "int", "status": {"type": "enum"}}}
    }
    with pytest.raises(ValueError, match="must include 'enum' name"):
        ContractValidator().validate(bad)


def test_enum_field_with_undefined_enum_raises():
    bad = {
        "module": {"name": "X", "namespace": "App\\X"},
        "entities": {"User": {"id": "int", "status": {"type": "enum", "enum": "UserStatus"}}}
    }
    with pytest.raises(ValueError, match="references undefined enum"):
        ContractValidator().validate(bad)
