import pytest

from src.product import Product
from src.product_iterator import ProductIterator


def test_product_iterator(first_category_1):
    it = ProductIterator(first_category_1)
    iter(it)
    assert it.index == 0

    first = next(it)
    assert isinstance(first, Product)
    assert first.name == "огурец"

    second = next(it)
    assert isinstance(second, Product)
    assert second.name == "яблоки"

    with pytest.raises(StopIteration):
        next(it)
