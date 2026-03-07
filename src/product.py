class Product:
    name: str
    description: str
    price: float
    quantity: int


    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


    def __add__(self, other):
        return self.quantity*self.__price + other.quantity*other.__price

    @classmethod
    def new_product(cls, name, description, price, quantity):
        return cls (name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price:float):
        if new_price <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        self.__price = float(new_price)


if __name__ == "__main__":
    product = Product("огурец", "овощь", 56.5, 5)

    print(product.name)
    print(product.description)
    print(product.price)
    print(product.quantity)

    product_2 = Product.new_product("манго", "фрукт", 76.5, 3)

    print(product_2.name)
    print(product_2.description)
    print(product_2.price)
    print(product_2.quantity)

    product_2.price = 50
    print(product_2.name)
    print(product_2.description)
    print(product_2.price)
    print(product_2.quantity)

print(Product)
