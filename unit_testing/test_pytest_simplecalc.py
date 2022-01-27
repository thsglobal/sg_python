# Pytest framework
from unit_testing.simplecalc import SimpleCalc
import pytest


@pytest.fixture
def calc():
    return SimpleCalc()


def test_calc_add(calc):
    assert calc.add(2, 6) == 8


def test_calc_subtract(calc):
    assert calc.subtract(2, 6) == -4


def test_calc_multiply(calc):
    assert calc.multiply(2, 6) == 12


def test_calc_divide(calc):
    assert pytest.approx(calc.divide(2, 6), 0.00001) == 1 / 3


def test_calc_divide_by_zero_raises_error():
    calc = SimpleCalc()
    with pytest.raises(ZeroDivisionError):
        calc.divide(1,0)