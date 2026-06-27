from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import torch


@dataclass
class SyntheticGraphLoader:
    num_nodes: int = 50
    num_features: int = 32
    seed: int = 42

    def load(self):
        g = _SyntheticGraph(num_nodes=self.num_nodes, num_features=self.num_features, seed=self.seed)
        return g


class _SyntheticGraph:
    def __init__(self, num_nodes: int, num_features: int, seed: int) -> None:
        g = torch.Generator().manual_seed(seed)
        self.num_nodes = num_nodes
        self.num_features = num_features


        # Node features
        self.x = torch.randn((num_nodes, num_features), generator=g)

        # Random edges (undirected-ish)
        num_edges = max(num_nodes * 2, 10)
        src = torch.randint(0, num_nodes, (num_edges,), generator=g)
        dst = torch.randint(0, num_nodes, (num_edges,), generator=g)
        edge_index = torch.stack([src, dst], dim=0)
        self.edge_index = edge_index
        self.num_edges = int(edge_index.shape[1])

        # Basic edge labels for quick link prediction training
        self.edge_label_index = edge_index
        self.edge_label = torch.randint(0, 2, (edge_index.shape[1],)).float()


    def to(self, device: str):
        self.x = self.x.to(device)
        self.edge_index = self.edge_index.to(device)
        self.edge_label_index = self.edge_label_index.to(device)
        self.edge_label = self.edge_label.to(device)
        return self


