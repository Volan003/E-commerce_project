import pytest


def test_category_init(first_category, second_category):
    assert first_category.name == "яблоко"
    assert first_category.description == "фрукт"
    assert len(first_category.products) == 21

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5


def test_category_init_ (category):
    assert category.name == "помидор"
    assert category.description == "овощи"
#    assert category.products == []


def test_category_str(first_category):
    #print(first_category) #проверяем, какой результат возвращается
    assert str(first_category) == "яблоко, количество продуктов: 2 шт."

# def test_product_iterator(product_iterator):
#     iter(product_iterator)
#     assert product_iterator.index == 0
#     assert next(product_iterator).name == "огурец"
#     assert next(product_iterator).name == "яблоки"
#
#     with pytest.raises(StopIteration):
#         next(task_iterator)