import yaml
from pathlib import Path

class ConfigLoader:
    def load(self, path: str) -> dict:
        config_path = Path(path)

        if not config_path.exists():
            return {}

        with config_path.open() as f:
            return yaml.safe_load(f) or {}
