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
        ("V", "I", "VI"),
        ("I", "V", "VI"),
        ("III", "IIII", "VII"),
        ("IIII", "III", "VII"),
        ("II", "V", "VII"),
    ],
)
def test1(a: str, b: str, expected: str) -> None:
    assert add(a, b) == expected
