import pytest
from src.product import Product
from src.category import Category


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