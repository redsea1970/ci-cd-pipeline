# ci-cd-pipeline

Демо CI/CD-пайплайна: проверка кода (black, mypy, pytest), сборка Docker-образа и публикация в GHCR.

## Что внутри

- `src/app/main.py` — функции `add(a, b) -> int` и `health() -> dict[str, str]`.
- `tests/test_main.py` — юнит-тесты (2 passed).
- `pyproject.toml` — setuptools (src-layout), black (line-length=100, py311), mypy (strict), pytest (pythonpath=src).
- `requirements-dev.txt` — pytest, black, mypy.
- `Dockerfile` — `python:3.12-slim`, `pip install -e .`, `CMD python -c print(health())`.
- `.github/workflows/ci.yml` — джобы `test` (black --check, mypy, pytest) и `docker` (needs: test, main, push в ghcr.io через GITHUB_TOKEN).

## Локальный запуск

    python -m venv venv
    .\venv\Scripts\Activate.ps1
    pip install -r requirements-dev.txt
    pip install -e .
    black --check .
    mypy src tests
    pytest -q

## Docker

    docker build -t ci-cd-pipeline .
    docker run --rm ci-cd-pipeline

## CI/CD

- Actions: https://github.com/redsea1970/ci-cd-pipeline/actions
- GHCR: https://github.com/redsea1970/ci-cd-pipeline/pkgs/container/ci-cd-pipeline

Пуш в `main` → прогон `test` → при успехе сборка и публикация `ghcr.io/redsea1970/ci-cd-pipeline:latest`.
