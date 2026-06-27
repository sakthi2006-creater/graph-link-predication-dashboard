from __future__ import annotations

from typing import Any, Dict


class CoraDatasetLoader:
    """Lightweight Cora loader.

    The original research repo likely used PyG datasets, but for local smoke tests
    (and to avoid network downloads), we fall back to a synthetic graph.
    """

    def __init__(self, config: Dict[str, Any]):
        self.config = config

    def load(self):
        from .synthetic_loader import SyntheticGraphLoader

        # Choose defaults close to typical Cora sizes but keep tiny for fast tests.
        num_nodes = int(self.config.get("synthetic", {}).get("cora_num_nodes", 270))
        num_features = int(self.config.get("synthetic", {}).get("cora_num_features", 1433))
        # keep memory bounded
        num_features = min(num_features, 128)
        return SyntheticGraphLoader(num_nodes=num_nodes, num_features=num_features, seed=42).load()

