from __future__ import annotations

from typing import Any, Dict

import torch
import torch.nn as nn


class GraphSAGEBaseline(nn.Module):
    """Baseline model for smoke tests."""

    def __init__(self, hidden_dim: int = 64):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.lin = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
        )

    def forward(self, graph: Any) -> Dict[str, torch.Tensor]:
        x = graph.x
        # If input feature size differs, project.
        if x.shape[1] != self.hidden_dim:
            proj = nn.Linear(x.shape[1], self.hidden_dim, bias=False).to(x.device)
            x = proj(x)
        node_emb = self.lin(x)
        return {"node_emb": node_emb}

