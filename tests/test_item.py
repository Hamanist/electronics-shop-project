"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError


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


def test_len_name():
    item_1 = Item('Смартфон', 5_000, 5)
    item_1.name = 'СуперСмартфон'
    assert len(item_1.name) == 10
    item_1.name = 'Супер'
    assert len(item_1.name) == 5


def test_string_to_number():
    assert Item.string_to_number('2.0') == 2
    assert Item.string_to_number('3') == 3
    assert Item.string_to_number('4.6') == 4


def test_repr():
    item = Item("Смартфон", 10000, 20)
    assert item.__repr__() == "Item('Смартфон', 10000, 20)"
    assert type(repr(item)) == str


def test_srt():
    item = Item("Смартфон", 10000, 20)
    assert item.__str__() == "Смартфон"
    assert len(str(item)) == 8


def test_raise():
    item = Item("Смартфон", 10000, 20)
    with pytest.raises(FileNotFoundError):
        item.instantiate_from_csv("tutu.csv")


def test_raise_2():
    item = Item("Смартфон", 10000, 20)
    lines_1 = 'name,price \n'
    lines_2 = 'Смартфон,100 \n'
    with open('../src/tests_for_items.csv', 'w') as file:
        file.writelines([lines_1, lines_2])
    with pytest.raises(InstantiateCSVError, match='Файл item.csv поврежден'):
        item.instantiate_from_csv('../src/tests_for_items.csv')
