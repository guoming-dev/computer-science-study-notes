import pytest
from fuel import convert
from fuel import gauge

def test_fraction():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/1") == 100

def test_value_error():
    with pytest.raises(ValueError):
        convert("5/4")

def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_gauge_result():
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
