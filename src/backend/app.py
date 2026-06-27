from __future__ import annotations

from fastapi import FastAPI

app = FastAPI(title="Graph Foundation Model API")

# ADD THIS
@app.get("/")
def home():
    return {
        "message": "Graph Foundation Model API is running!",
        "docs": "/docs",
        "health": "/health"
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/dataset/{name}")
def dataset(name: str):
    return {
        "name": name,
        "status": "available"
    }