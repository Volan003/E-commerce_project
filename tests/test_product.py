from src.product import Product


def test_products_init(products):
    assert products.name == "огурец"
    assert products.description == "овощ"


def test_products_create():
    product = Product("манго", "фрукт", 76.5, 3)
    product.name = "манго"
    product.description = "фрукт"
    product.price = 76.5
    product.quantity = 3


def test_products_update(capsys, products):
    products.price = 80
    assert products.price == 80
