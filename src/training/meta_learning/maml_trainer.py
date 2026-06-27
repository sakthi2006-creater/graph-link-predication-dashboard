from __future__ import annotations

from typing import List, Optional

import torch

from ...data.loaders.synthetic_loader import SyntheticGraphLoader
from ...models import GraphFoundationModel


class MAMLTrainer:
    def __init__(self, device: Optional[str] = None) -> None:
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.model = GraphFoundationModel(input_dim=32, hidden_dim=64).to(self.device)
        self.optim = torch.optim.Adam(self.model.parameters(), lr=1e-3)
        self.loss_fn = torch.nn.BCEWithLogitsLoss()

    def meta_fit(self, num_epochs: int = 1, source_domains: Optional[List[str]] = None):
        source_domains = source_domains or ["cora"]
        for _ in range(int(num_epochs)):
            # Simplified inner/outer loops for smoke test.
            for _task in range(2):
                g = SyntheticGraphLoader(num_nodes=40, num_features=32, seed=42).load().to(self.device)
                out = self.model(g)
                scores = self.model.link_predictor(out["node_emb"], g.edge_label_index)
                loss = self.loss_fn(scores, g.edge_label)
                self.optim.zero_grad()
                loss.backward()
                self.optim.step()
        return loss.item()

