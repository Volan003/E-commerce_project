from src.product import Product


def test_products_init(products):
    assert products.name == "огурец"
    assert products.description == "овощ"


def test_product_str(products):
    #print(products)
    assert str(products) == "огурец, 56.5 руб. Остаток: 5 шт."


def test_product_add(product_all_price_1, product_all_price_2):
    assert product_all_price_1 + product_all_price_2 == 404.5
