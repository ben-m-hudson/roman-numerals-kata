import pytest

from roman import add


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("I", "I", "II"),
        ("I", "II", "III"),
        ("II", "I", "III"),
        ("II", "II", "IV"),
        ("II", "III", "V"),
        ("III", "II", "V"),
        ("III", "III", "VI"),
        ("V", "I", "VI"),
        ("I", "V", "VI"),
        ("III", "IV", "VII"),
        ("IV", "III", "VII"),
        ("II", "V", "VII"),
        ("II", "IX", "XI")
    ],
)
def test1(a: str, b: str, expected: str) -> None:
    assert add(a, b) == expected
