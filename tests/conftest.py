import pytest
from src.product import Product
from src.category import Category
from src.product_iterator import ProductIterator


@pytest.fixture
def first_category():
    return Category (
        name = "яблоко",
        description = "фрукт",
        products = ["антоновка","белый налив"]
    )


@pytest.fixture
def second_category():
    return Category (
        name = "помидор",
        description = "овощи",
        products = ["японский","китайский", "европейский"]
    )


@pytest.fixture
def products():
    return Product("огурец", "овощ", 56.5, 5)

@pytest.fixture
def category():
    return Category("помидор", "овощи")


@pytest.fixture
def product_all_price_1():
    return Product("огурец", "овощь", 56.5, 5)


@pytest.fixture
def product_all_price_2():
    return Product("яблоки", "фрукт", 30.5, 4)


@pytest.fixture
def product_iterator_1(first_category):
    return ProductIterator(first_category)

@pytest.fixture
def first_category_1():
    p1 = Product("огурец", "овощ", 56.5, 5)
    p2 = Product("яблоки", "фрукт", 40.0, 3)
    return Category("category", "desc", [p1, p2])