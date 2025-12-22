import yaml
from pathlib import Path

class ContractParser:
    def parse(self, path: str) -> dict:
        contract_path = Path(path)

        if not contract_path.exists():
            raise FileNotFoundError(f"Contract not found: {path}")

        with contract_path.open() as f:
            data = yaml.safe_load(f)

        if not isinstance(data, dict):
            raise ValueError("Invalid contract format")

        return data
