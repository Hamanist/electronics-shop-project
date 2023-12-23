import pytest

from src.phone import Phone


def test_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone1.number_of_sim = 0
    assert phone1.number_of_sim != 0

def test_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)

    assert phone1.__repr__() == "Phone('iPhone 14', 120000, 5, 2)"
    assert type(repr(phone1)) == str
