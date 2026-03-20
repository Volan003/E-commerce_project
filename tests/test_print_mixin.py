from src.product import Product


def test_print_mixin(capsys):
    Product("огурец", "овощ", 56.5, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(name='огурец', description='овощ', price=56.5, quantity=5)"
