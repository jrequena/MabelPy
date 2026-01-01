import pytest
from core.contract.validator import ContractValidator

def test_validate_valid_entities_format():
    validator = ContractValidator()
    contract = {
        "entities": {
            "User": {
                "id": "int",
                "email": "string"
            }
        }
    }
    # Should not raise exception
    validator.validate(contract)

def test_validate_valid_entities_contract():
    validator = ContractValidator()
    contract = {
        "entities": {
            "User": {
                "id": "int",
                "email": {"type": "Email", "nullable": True}
            }
        }
    }
    validator.validate(contract)

def test_validate_invalid_type():
    validator = ContractValidator()
    contract = {
        "entities": {
            "User": {
                "id": "UnknownType"
            }
        }
    }
    with pytest.raises(ValueError, match="Unknown type referenced"):
        validator.validate(contract)

def test_validate_invalid_enum_reference():
    validator = ContractValidator()
    contract = {
        "entities": {
            "User": {
                "status": {"type": "enum", "enum": "UndefinedEnum"}
            }
        }
    }
    with pytest.raises(ValueError, match="references undefined enum"):
        validator.validate(contract)

def test_validate_valid_enum():
    validator = ContractValidator()
    contract = {
        "enums": {
            "UserStatus": {
                "type": "string",
                "values": ["ACTIVE", "INACTIVE"]
            }
        },
        "entities": {
            "User": {
                "status": "UserStatus"
            }
        }
    }
    validator.validate(contract)

def test_validate_constraints():
    validator = ContractValidator()
    contract = {
        "entities": {
            "User": {
                "age": {"type": "int", "min": 18, "max": 120}
            }
        }
    }
    validator.validate(contract)

def test_validate_invalid_constraints():
    validator = ContractValidator()
    contract = {
        "entities": {
            "User": {
                "age": {"type": "int", "min": "invalid"}
            }
        }
    }
    with pytest.raises(ValueError, match="must be numeric"):
        validator.validate(contract)

def test_validate_invalid_default_type():
    validator = ContractValidator()
    contract = {
        "entities": {
            "User": {
                "age": {"type": "int", "default": "not-an-int"}
            }
        }
    }
    with pytest.raises(ValueError, match="must be an integer"):
        validator.validate(contract)

def test_validate_invalid_enum_default():
    validator = ContractValidator()
    contract = {
        "enums": {
            "UserStatus": {
                "type": "string",
                "values": ["ACTIVE", "INACTIVE"]
            }
        },
        "entities": {
            "User": {
                "status": {"type": "UserStatus", "default": "INVALID"}
            }
        }
    }
    with pytest.raises(ValueError, match="is not a valid case for enum"):
        validator.validate(contract)

def test_validate_empty_entities():
    validator = ContractValidator()
    contract = {
        "entities": {}
    }
    with pytest.raises(ValueError, match="define a non-empty 'entities' mapping"):
        validator.validate(contract)
