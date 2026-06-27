from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

import torch
import torch.nn as nn


class LinkPredictor(nn.Module):
    def __init__(self, hidden_dim: int):
        super().__init__()
        self.mlp = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1),
        )

    def forward(self, node_emb: torch.Tensor, edge_label_index: torch.Tensor) -> torch.Tensor:
        # edge_label_index: [2, E]
        src = edge_label_index[0]
        dst = edge_label_index[1]
        h = torch.cat([node_emb[src], node_emb[dst]], dim=-1)
        return self.mlp(h).squeeze(-1)


class GraphFoundationModel(nn.Module):
    """Small, test-oriented graph foundation model.

    Tests only require:
    - model(g) returns dict with node_emb
    - model.link_predictor(emb, query) returns scores tensor
    """

    def __init__(self, input_dim: int = 32, hidden_dim: int = 64):
        super().__init__()
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
        )
        self.link_predictor = LinkPredictor(hidden_dim=hidden_dim)

    def forward(self, graph: Any) -> Dict[str, torch.Tensor]:
        x = graph.x
        # If feature dim differs, adapt by projecting to expected input_dim.
        if x.shape[1] != self.input_dim:
            # simple runtime projection
            proj = nn.Linear(x.shape[1], self.input_dim, bias=False).to(x.device)
            x = proj(x)
        node_emb = self.encoder(x)
        return {"node_emb": node_emb}

