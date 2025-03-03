import pytest # had to change interpreter to point at the one in .venv
from calculator.operations import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(1, 1) == 0

def test_multiply():
    assert multiply(5, 2) == 10

def test_divide():
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)