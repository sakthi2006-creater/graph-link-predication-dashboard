from __future__ import annotations

from typing import Optional

import torch
import torch.nn as nn

from ...data.loaders.synthetic_loader import SyntheticGraphLoader
from ...models import GraphFoundationModel


class FinetuneTrainer:
    def __init__(self, device: Optional[str] = None) -> None:
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.model = GraphFoundationModel(input_dim=32, hidden_dim=64).to(self.device)
        # Adapter-like head for smoke tests: train all params for simplicity.
        self.loss_fn = nn.BCEWithLogitsLoss()
        self.optim = torch.optim.Adam(self.model.parameters(), lr=1e-3)

    def fit(self, num_epochs: int = 1):
        graph = SyntheticGraphLoader(num_nodes=50, num_features=32).load().to(self.device)
        for _ in range(int(num_epochs)):
            out = self.model(graph)
            scores = self.model.link_predictor(out["node_emb"], graph.edge_label_index)
            loss = self.loss_fn(scores, graph.edge_label)
            self.optim.zero_grad()
            loss.backward()
            self.optim.step()
        return loss.item()

