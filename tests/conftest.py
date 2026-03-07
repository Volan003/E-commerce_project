import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator
from src.product_Smartphone import Smartphone
from src.product_LawnGrass import LawnGrass


@pytest.fixture
def first_category():
    return Category(
        name="яблоко",
        description="фрукт",
        products=["антоновка", "белый налив"]
    )


@pytest.fixture
def second_category():
    return Category(
        name="помидор",
        description="овощи",
        products=["японский", "китайский", "европейский"]
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


@pytest.fixture
def product_smartphone():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                         "S23 Ultra", 256, "Серый")


@pytest.fixture
def product_smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def product_grass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def product_grass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")