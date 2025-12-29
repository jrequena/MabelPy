import json
import hashlib
import subprocess
from datetime import datetime
from pathlib import Path

class MetadataManager:
    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.metadata_file = output_dir / ".mabel_metadata.json"

    def record_generation(self, contract_path: Path):
        contract_content = contract_path.read_text()
        contract_hash = hashlib.sha256(contract_content.encode()).hexdigest()
        
        commit_hash = self._get_git_commit()
        timestamp = datetime.now().isoformat()
        
        entry = {
            "timestamp": timestamp,
            "contract": str(contract_path),
            "contract_hash": contract_hash,
            "commit": commit_hash
        }
        
        history = self._load_history()
        history.append(entry)
        
        with open(self.metadata_file, "w") as f:
            json.dump(history, f, indent=4)

    def _get_git_commit(self):
        try:
            return subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
        except Exception:
            return "unknown"

    def _load_history(self):
        if self.metadata_file.exists():
            try:
                return json.loads(self.metadata_file.read_text())
            except Exception:
                return []
        return []
