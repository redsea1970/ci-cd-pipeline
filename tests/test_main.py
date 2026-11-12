from app.main import add, health


def test_add() -> None:
    assert add(2, 3) == 5


def test_health() -> None:
    assert health() == {"status": "ok"}
