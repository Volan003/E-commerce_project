from src.product import Product
from src.category import Category

class ProductIterator:
    def __init__(self, category_obj):
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.category.products_in_list):
            item = self.category.products_in_list[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

if __name__ == "__main__":
    product_1 = Product("огурец", "овощь", 56.5, 5)
    product_2 = Product("яблоки", "фрукт", 30.5, 4)
    product_3 = Product("апельсины", "фрукт", 70.5, 8)
    product_4 = Product("манго", "фрукт", 65.5, 12)

    category = Category("Фрукты и овощи", "Различные продукты", [product_1, product_2, product_3, product_4])

    iterator = ProductIterator(category)

    for product in iterator:
        print(product)
    print()

    for product in iterator:
        print(product)