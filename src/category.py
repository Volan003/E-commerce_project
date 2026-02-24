from src.product import Product

class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)


    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    @property
    def products(self):
        """Возвращает строковое представление всех продуктов."""
        if not self.__products:
            return "Нет продуктов"
        return "\n".join(str(product) for product in self.__products)

    @property
    def products_in_list(self):
        """Возвращает список продуктов (для итератора)."""
        return self.__products

    def add_product(self, product: Product):
        """Добавляет продукт в категорию."""
        self.__products.append(product)
        Category.product_count += 1


if __name__ == "__main__":
    # Создаём объекты Product (предполагается, что класс Product уже определён)
    product_1 = Product("помидор японский", "овощ", 100.0, 5)
    product_2 = Product("помидор китайский", "овощ", 90.0, 10)
    product_3 = Product("помидор европейский", "овощ", 120.0, 8)

    # Создаём категорию с продуктами
    category = Category(
        "помидор",
        "овощи",
        [product_1, product_2, product_3]
    )

    print(category)
    print()
    print(category.name)
    print(category.description)
    print(category.products)  # Строковое представление продуктов
    print("Список продуктов:", category.products_in_list)  # Сам список
    print("Количество категорий:", Category.category_count)
    print("Общее количество продуктов:", Category.product_count)