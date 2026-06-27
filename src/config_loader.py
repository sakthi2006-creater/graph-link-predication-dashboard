from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional

import yaml


DEFAULT_CONFIG_PATH = Path(__file__).resolve().parents[1] / "config.yaml"


def load_config(config_path: Optional[str] = None) -> Dict[str, Any]:
    """Load YAML config.

    The tests expect this function to exist at `src.config_loader.load_config`.
    """

    path = Path(config_path) if config_path else DEFAULT_CONFIG_PATH
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data

