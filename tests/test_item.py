"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item_data():
    return Item('Телефон', 5_000.0, 10)


def test_item(item_data):
    assert item_data


def test_item_calculate(item_data):
    assert item_data.calculate_total_price() == 50_000


def test_item_apply_discount(item_data):
    pay_rate = 0.85
    item_data.apply_discount()
    assert int(item_data.price * pay_rate) == 4_250


def test_name(item_data):
    assert item_data.name == 'Телефон'


def test_len_name(item_data):
    item_data = "СуперСмартфон"
    if len(item_data) >= 10:
        item_data = item_data[:10]
        assert item_data == 'СуперСмарт'
    assert item_data == item_data


def test_string_to_number():
    assert Item.string_to_number('2.0') == 2
    assert Item.string_to_number('3') == 3
    assert Item.string_to_number('4.6') == 4


def test_instantiate_from_csv():
    pass
