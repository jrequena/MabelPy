import pytest
import shutil
from pathlib import Path
from core.generator.php_dto_generator import PhpDtoGenerator
from core.generator.php_enum_generator import PhpEnumGenerator
from core.config import MabelConfig

@pytest.fixture
def config():
    return MabelConfig.from_file()

def test_dto_generation_snapshot(config, snapshot, tmp_path):
    generator = PhpDtoGenerator(config)
    contract = {
        "entity": {"name": "User"},
        "fields": [
            {"name": "id", "type": "int"},
            {"name": "name", "type": "string"},
            {"name": "status", "type": "UserStatus"}
        ],
        "enums": {"UserStatus": {"type": "string", "values": ["ACTIVE"]}}
    }
    
    # Generate to tmp_path
    generator.generate(contract, tmp_path)
    
    # Check generated file
    domain_suffix = config.get_generator_config("entity").get("namespace_suffix", "Domain")
    generated_file = tmp_path / domain_suffix / "User.php"
    
    assert generated_file.exists()
    snapshot.assert_match(generated_file.read_text(), "UserDTO.php")

def test_enum_generation_snapshot(config, snapshot, tmp_path):
    generator = PhpEnumGenerator(config)
    enum_name = "UserStatus"
    enum_def = {
        "type": "string",
        "values": ["ACTIVE", "INACTIVE", "PENDING"]
    }
    
    generator.generate(enum_name, enum_def, tmp_path)
    
    domain_suffix = config.get_generator_config("entity").get("namespace_suffix", "Domain")
    generated_file = tmp_path / domain_suffix / "Enum" / "UserStatus.php"
    
    assert generated_file.exists()
    snapshot.assert_match(generated_file.read_text(), "UserStatusEnum.php")
