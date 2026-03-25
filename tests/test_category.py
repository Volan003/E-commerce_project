import pytest

from src.category import Category
from src.exceptions import ZeroProduct
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


def test_category_str_comprehensive():
    p1 = Product("яблоко", "фрукт", 60.0, 10)
    c1 = Category("яблоки", "Зелёные яблоки", [p1])
    assert str(c1) == "яблоки, количество продуктов: 10 шт."

    p2 = Product("груша", "фрукт", 70.0, 5)
    p3 = Product("слива", "фрукт", 50.0, 8)
    c2 = Category("груши и сливы", "Фрукты", [p2, p3])
    assert str(c2) == "груши и сливы, количество продуктов: 13 шт."

    c3 = Category("апельсины", "Цитрусовые", [])
    assert str(c3) == "апельсины, количество продуктов: 0 шт."


def test_category_add_product_error(first_category, products):
    assert len(first_category.products_in_list) == 2


def test_middle_price_count(first_category_1):
    assert first_category_1.middle_price_count() == 48.25


def test_add_product_successful(capsys):
    Category.category_count = 0
    Category.product_count = 0

    category = Category("category", "desc", [])
    p = Product("огурец", "овощ", 56.5, 5)

    category.add_product(p)

    assert len(category.products_in_list) == 1
    assert category.products_in_list[0] is p

    captured = capsys.readouterr()
    assert "Продукт добавлен" in captured.out
    assert "Обработка добавления продукта завершена" in captured.out


def test_price_setter_zero_value(product_all_price_1):
    product_all_price_1.price = 0
    assert product_all_price_1.price == 0.0
    product_all_price_1.price = -10
    assert product_all_price_1.price == -10.0