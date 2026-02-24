from src.product import Product

class Category:
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products = None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f'{product.name}, {product.price} руб., Остаток: {product.quantity} шт.\n'
        return product_str

    @property
    def products_in_list(self):
        return self.__products

    def add_product(self, product: Product):
        self.__products.append (product)
        Category.product_count += 1


if __name__ == "__main__":
    product_1 = Product("огурец", "овощь", 56.5, 5)
    product_2 = Product("яблоки", "фрукт", 30.5, 4)
    product_3 = Product("апельсины", "фрукт", 70.5, 8)
    product_4 = Product("манго", "фрукт", 65.5, 12)

    category = Category("Фрукты и овощи", "Различные продукты", [product_1, product_2, product_3, product_4])

    print(category.name)
    print(category.description)
    print(category.products)
    print(Category.category_count)
    print(Category.product_count)

    product_5 = Product("огурец", "овоЩЬ", 56.5, 5)
    category.add_product(product_5)

    print(category.products)
    print(Category.product_count)