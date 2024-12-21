import pytest
from .equations import equations


@pytest.mark.parametrize(
        "equation, want_result", 
    [
        ("y + 3 = 15", "y = 12"),
        ("18 + x = 20", "x = 2"),
        ("18 + 15 = x", "x = 33"),
        ("x - 3 = 15", "x = 18"),
        ("18 - x = 12", "x = 6"),
        ("18 - 12 = x", "x = 6"),
        ("x * 3 = 15", "x = 5"),
        ("18 * x = 36", "x = 2"),
        ("18 * 3 = x", "x = 54"),
        ("x / 3 = 15", "x = 45"),
        ("18 / x = 6", "x = 3"),
        ("18 / 3 = x", "x = 6"),
        # ("18 / 4 = x", "x = 4.5"),
    ]
)
def test_equations(equation, want_result):
    assert equations.equation(equation) == want_result
