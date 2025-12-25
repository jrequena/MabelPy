import yaml
from pathlib import Path


class ConfigLoader:
    def __init__(self, path: str = "mabel.yaml"):
        self.path = Path(path)

    def load(self) -> dict:
        if not self.path.exists():
            return {}

        with self.path.open() as f:
            return yaml.safe_load(f) or {}
