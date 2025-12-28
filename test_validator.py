from core.config import ConfigLoader, MabelConfig
from core.config.validator import ConfigValidator
import os

def test_validator():
    print("Testing Validator...")
    
    # 1. Test with current valid mabel.yaml
    try:
        config = ConfigLoader("mabel.yaml").load()
        print("✓ Current mabel.yaml is valid")
    except ValueError as e:
        print(f"✗ Current mabel.yaml failed: {e}")

    # 2. Test with missing section
    invalid_config = {
        "project": {"name": "Test"}
    }
    errors = ConfigValidator.validate(invalid_config)
    if "Missing required section: 'paths'" in errors:
        print("✓ Successfully detected missing 'paths' section")
    else:
        print("✗ Failed to detect missing 'paths' section")

    # 3. Test with invalid framework
    invalid_framework_config = {
        "project": {"name": "Test", "namespace": "Test", "framework": "invalid"},
        "paths": {
            "source_root": "src",
            "domain": "src/Domain",
            "application": "src/Application",
            "infrastructure": "src/Infrastructure",
            "tests": "tests"
        },
        "generators": {}
    }
    errors = ConfigValidator.validate(invalid_framework_config)
    if any("Invalid framework 'invalid'" in e for e in errors):
        print("✓ Successfully detected invalid framework")
    else:
        print(f"✗ Failed to detect invalid framework. Errors: {errors}")

if __name__ == "__main__":
    test_validator()
