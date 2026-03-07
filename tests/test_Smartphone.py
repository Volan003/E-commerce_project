import pytest

def test_product_smartphone(product_smartphone):
    assert product_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert product_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert product_smartphone.price == 180000.0
    assert product_smartphone.quantity == 5
    assert product_smartphone.efficiency == 95.5
    assert product_smartphone.model == "S23 Ultra"
    assert product_smartphone.memory == 256
    assert product_smartphone.color == "Серый"

def test_product_smartphone_add(product_smartphone, product_smartphone2):
    assert product_smartphone + product_smartphone2 == 2580000.0


def test_product_smartphone_add_error(product_smartphone):
    with pytest.raises(TypeError):
        product_smartphone + 1