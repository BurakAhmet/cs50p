from fuel import convert, gauge
import pytest


def test_convert_value():
    with pytest.raises(ValueError):
        convert("dog/cat")


def test_convert_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_correct_value():
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("50/100") == 50 and gauge(50) == "50%"
    assert convert("99/100") == 99 and gauge(99) == "F"
