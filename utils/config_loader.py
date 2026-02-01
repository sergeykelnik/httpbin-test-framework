import os
import yaml
from pathlib import Path
from functools import reduce
from typing import Any


class ConfigLoader:
    """Load configuration from YAML file"""

    def __init__(self):
        self.config = self._load_yaml()

    def _load_yaml(self) -> dict:
        """Load configuration from YAML file"""
        yaml_path = Path(__file__).parent.parent / 'config' / 'config.yaml'
        try:
            with open(yaml_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or {}
        except FileNotFoundError:
            return {}

    def get(self, key: str, default: Any = None) -> Any:
        """Get nested configuration value
         using dot notation (e.g., 'api.base_url')"""
        try:
            return reduce(lambda d, k: d[k], key.split('.'), self.config)
        except (KeyError, TypeError):
            return default

    @property
    def base_url(self) -> str:
        return os.getenv('BASE_URL',
                         self.get('api.base_url', 'https://httpbin.org'))

    @property
    def timeout(self) -> int:
        return int(self.get('api.timeout', 30))

    @property
    def max_retry_attempts(self) -> int:
        return int(self.get('retry.max_attempts', 3))

    @property
    def retry_delay(self) -> float:
        return float(self.get('retry.delay', 1))

    @property
    def retry_backoff_factor(self) -> float:
        return float(self.get('retry.backoff_factor', 2))


config = ConfigLoader()
