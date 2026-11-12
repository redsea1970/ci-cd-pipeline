"""Minimal service with a health endpoint (for CI/CD demo)."""

from __future__ import annotations


def add(a: int, b: int) -> int:
    """Return a + b."""
    return a + b


def health() -> dict[str, str]:
    """Return a health payload."""
    return {"status": "ok"}
