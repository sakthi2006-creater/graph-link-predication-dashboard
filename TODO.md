# TODO

## Blocking issue

- [ ] Obtain the complete repository content that includes the missing `src/` directory (and any other required implementation folders).

## Once complete project root is available

- [ ] Inspect current file structure (src/backend/streamlit/training/evaluation) and map modules required by `test_run.py` and `test_train.py`.
- [ ] Create/verify a local virtual environment and install dependencies from `requirements.txt`.
- [ ] Run `python test_train.py` and `python test_run.py` and capture errors.
- [ ] Fix import/path/packaging issues (e.g., missing `__init__.py`, incorrect module names).
- [ ] Fix runtime issues until all entrypoints run:
  - [ ] `python test_train.py`
  - [ ] `python test_run.py`
  - [ ] `pytest`
  - [ ] `uvicorn src.backend.app:app --reload`
  - [ ] `streamlit run src/streamlit_app/app.py`
- [ ] Update `requirements.txt`, `pyproject.toml`, and `README.md` with a clean, reproducible setup.
- [ ] Add `.env.example` if missing.
- [ ] Validate basic smoke tests and document how to run from a clean machine.
