from itertools import product

from src.category import Category
from src.product import Product


def test_category_init(first_category, second_category):
    assert first_category.name == "яблоко"
    assert first_category.description == "фрукт"
    assert len(first_category.products) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5


def test_category_init_(category):
    assert category.name == "помидор"
    assert category.description == "овощи"
    # assert category.products == []


def test_category_init_1(first_category, second_category):
    assert first_category.name == "яблоко"
    assert first_category.description == "фрукт"
    assert len(first_category.products_in_list) == 2

    assert first_category.category_count == 5
    assert second_category.category_count == 5

    assert first_category.product_count == 10
    assert second_category.product_count == 10


# def test_category_products_property():
#     p1 = Product("огурец", "овощ", 56.5, 5)
#     c = Category("помидор", "овощи", [p1])
#
#     # Проверяем корректность вывода
#     expected = "огурец, 56.5 руб. Остаток: 5 шт.\n"
#     assert c.products == expected

def test_category_add_product_error(first_category, products):
    assert len(first_category.products_in_list) == 2