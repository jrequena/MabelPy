from pathlib import Path
from typing import Optional, Dict, Any
from .loader import ConfigLoader


class MabelConfig:
    def __init__(self, config_data: Optional[Dict[str, Any]] = None):
        self._config = config_data or ConfigLoader().load()

    @classmethod
    def from_file(cls, path: str = "mabel.yaml") -> "MabelConfig":
        return cls(ConfigLoader(path).load())

    @property
    def project_name(self) -> str:
        return self._config["project"]["name"]

    @property
    def project_namespace(self) -> str:
        return self._config["project"]["namespace"]

    @property
    def framework(self) -> str:
        return self._config["project"]["framework"]

    @property
    def php_version(self) -> str:
        return self._config["project"]["php_version"]

    @property
    def path_domain(self) -> Path:
        return Path(self._config["paths"]["domain"])

    @property
    def path_application(self) -> Path:
        return Path(self._config["paths"]["application"])

    @property
    def path_infrastructure(self) -> Path:
        return Path(self._config["paths"]["infrastructure"])

    @property
    def path_tests(self) -> Path:
        return Path(self._config["paths"]["tests"])

    @property
    def path_snapshots(self) -> Path:
        return Path(self._config["paths"]["snapshots"])

    def get_generator_config(self, name: str) -> Dict[str, Any]:
        return self._config["generators"].get(name, {})

    def get(self, key: str, default: Any = None) -> Any:
        keys = key.split(".")
        value = self._config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
        return value if value is not None else default

    def to_dict(self) -> Dict[str, Any]:
        return self._config.copy()
