import pytest

from roman import add


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("I", "I", "II"),
        ("I", "II", "III"),
        ("II", "I", "III"),
        ("II", "II", "IIII"),
        ("II", "III", "V"),
        ("III", "II", "V"),
        ("III", "III", "VI"),
    ],
)
def test1(a: str, b: str, expected: str) -> None:
    assert add(a, b) == expected
