from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

from .loaders.cora_loader import CoraDatasetLoader


@dataclass
class DataPipeline:
    config: Dict[str, Any]

    def load_dataset(self, name: str):
        name = name.lower()
        if name == "cora":
            return CoraDatasetLoader(config=self.config).load()
        # Fallback to synthetic graph
        from .loaders.synthetic_loader import SyntheticGraphLoader

        num_nodes = int(self.config.get("synthetic", {}).get("num_nodes", 50))
        num_features = int(self.config.get("synthetic", {}).get("num_features", 32))
        return SyntheticGraphLoader(num_nodes=num_nodes, num_features=num_features).load()

