import pytest
from src.product import Product
from tests.conftest import product_iterator_1


def test_product_iterator(product_iterator_1):
    iter(product_iterator_1)
    assert product_iterator_1.index == 0

    # first = next(product_iterator_1)
    # assert isinstance(first, Product)
    # assert first.name == "огурец"
    #
    # second = next(product_iterator)
    # assert isinstance(second, Product)
    # assert second.name == "яблоки"
    #
    # with pytest.raises(StopIteration):
    #     next(product_iterator)