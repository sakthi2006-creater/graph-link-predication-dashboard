from __future__ import annotations

from fastapi import FastAPI

app = FastAPI(title="Graph Foundation Model API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/dataset/{name}")
def dataset(name: str):
    return {"name": name, "status": "available"}

