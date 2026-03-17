import pytest


def test_product_grass(product_grass):
    assert product_grass.name == "Газонная трава"
    assert product_grass.description == "Элитная трава для газона"
    assert product_grass.price == 500.0
    assert product_grass.quantity == 20
    assert product_grass.country == "Россия"
    assert product_grass.germination_period == "7 дней"
    assert product_grass.color == "Зеленый"


def test_product_grass_add(product_grass, product_grass2):
    assert product_grass + product_grass2 == 16750.0


def test_product_grass_add_error(product_grass):
    with pytest.raises(TypeError):
        product_grass + 1
