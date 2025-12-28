import pytest
import yaml
from pathlib import Path
from core.config import ConfigLoader, MabelConfig, ConfigValidator

def test_default_config_loading():
    # Test loading with non-existent file uses defaults
    loader = ConfigLoader("non_existent.yaml")
    config = loader.load()
    assert config["project"]["name"] == "MabelApp"
    assert config["project"]["framework"] == "zend"

def test_config_merge(tmp_path):
    # Create a partial config file
    config_file = tmp_path / "mabel.yaml"
    user_config = {
        "project": {
            "name": "CustomApp",
            "framework": "laravel"
        }
    }
    with open(config_file, "w") as f:
        yaml.dump(user_config, f)
    
    loader = ConfigLoader(str(config_file))
    config = loader.load()
    
    assert config["project"]["name"] == "CustomApp"
    assert config["project"]["framework"] == "laravel"
    # Ensure default paths are still there
    assert config["paths"]["domain"] == "src/Domain"

def test_config_validator_missing_section():
    invalid_config = {"project": {}}
    errors = ConfigValidator.validate(invalid_config)
    assert any("Missing required section: 'paths'" in e for e in errors)
    assert any("Missing required section: 'generators'" in e for e in errors)

def test_config_validator_invalid_framework():
    invalid_config = {
        "project": {"name": "Test", "namespace": "Test", "framework": "cakephp"},
        "paths": {
            "source_root": "src", "domain": "d", "application": "a", 
            "infrastructure": "i", "tests": "t"
        },
        "generators": {"entity": {"enabled": True}}
    }
    errors = ConfigValidator.validate(invalid_config)
    assert any("Invalid framework 'cakephp'" in e for e in errors)

def test_mabel_config_properties(tmp_path):
    config_file = tmp_path / "mabel.yaml"
    user_config = {
        "project": {"name": "TestApp", "namespace": "AppTest", "framework": "zend", "php_version": "8.3"},
        "paths": {"domain": "domain_path", "application": "app_path", "infrastructure": "infra_path", "tests": "test_path", "source_root": "src", "snapshots": "snaps"},
        "generators": {"entity": {"enabled": True}}
    }
    with open(config_file, "w") as f:
        yaml.dump(user_config, f)
    
    mabel_config = MabelConfig.from_file(str(config_file))
    
    assert mabel_config.project_name == "TestApp"
    assert mabel_config.project_namespace == "AppTest"
    assert mabel_config.framework == "zend"
    assert mabel_config.php_version == "8.3"
    assert str(mabel_config.path_domain) == "domain_path"
    assert mabel_config.get_generator_config("entity")["enabled"] is True
    assert mabel_config.get("project.name") == "TestApp"
    assert mabel_config.get("non.existent", "default") == "default"
