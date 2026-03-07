import pytest


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
#    assert category.products == []


def test_category_str(product_all_price_2):
    assert str(product_all_price_2) == "яблоки, 30.5 руб. Остаток: 4 шт."
