import yaml
from pathlib import Path
from .validator import ConfigValidator


class ConfigLoader:
    DEFAULT_CONFIG = {
        "project": {
            "name": "MabelApp",
            "namespace": "App",
            "framework": "zend",
            "php_version": "8.2",
        },
        "paths": {
            "source_root": "src",
            "domain": "src/Domain",
            "application": "src/Application",
            "infrastructure": "src/Infrastructure",
            "tests": "tests",
            "snapshots": "tests/snapshots",
        },
        "generators": {
            "entity": {
                "enabled": True,
                "namespace_suffix": "Domain",
                "immutable": True,
                "validations": True,
            },
            "value_objects": {
                "enabled": True,
                "namespace_suffix": "Domain",
                "auto_types": ["Id", "Uuid", "Email"],
            },
            "repository": {
                "enabled": True,
                "interface_namespace_suffix": "Domain/Repository",
                "eloquent_namespace_suffix": "Infrastructure/Persistence/Eloquent",
            },
            "use_case": {
                "enabled": True,
                "namespace_suffix": "Domain/UseCase",
                "with_request_response": True,
            },
            "mapper": {
                "enabled": True,
                "namespace_suffix": "Infrastructure/Mapper",
            },
            "tests": {
                "enabled": True,
                "framework": "phpunit",
                "namespace_suffix": "Tests",
            },
        },
        "php": {
            "strict_types": True,
            "declare_strict": True,
            "readonly_default": True,
        },
    }

    def __init__(self, path: str = "mabel.yaml"):
        self.path = Path(path)

    def load(self) -> dict:
        config = self.DEFAULT_CONFIG.copy()
        
        if self.path.exists():
            with self.path.open() as f:
                user_config = yaml.safe_load(f) or {}
                config = self._deep_merge(config, user_config)
        
        errors = ConfigValidator.validate(config)
        if errors:
            raise ValueError("Invalid configuration in {}:\n- {}".format(
                self.path, "\n- ".join(errors)
            ))
            
        return config

    @staticmethod
    def _deep_merge(base: dict, override: dict) -> dict:
        for key, value in override.items():
            if isinstance(value, dict) and key in base and isinstance(base[key], dict):
                base[key] = ConfigLoader._deep_merge(base[key], value)
            else:
                base[key] = value
        return base
