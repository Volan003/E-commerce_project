def test_products_init (products):
    assert products.name == "огурец"
    assert products.description == "овощ"


def test_product_str(products):
    #print(products)
    assert str(products) == "Название продукта: огурец, Цена: 56.5 Остаток: 5"


# def test_product_add(product_quantity_price_1, product_quantity_price_2):
#     assert product_quantity_price_1 + product_quantity_price_2 == 9