class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        return (f"Product(name={self.name!r}, description={self.description!r}, "
                f"price={self._price!r}, quantity={self.quantity!r})")

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is Product:
            return self.quantity * self._price + other.quantity * other._price
        raise TypeError

    @classmethod
    def new_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        self._price = float(new_price)


if __name__ == "__main__":
    product = Product("огурец", "овощ", 56.5, 5)

    # print(product.name)
    # print(product.description)
    # print(product.price)
    # print(product.quantity)

    product_2 = Product.new_product("манго", "фрукт", 76.5, 3)

    # print(product_2.name)
    # print(product_2.description)
    # print(product_2.price)
    # print(product_2.quantity)
    #
    # product_2.price = 50
    # print(product_2.name)
    # print(product_2.description)
    # print(product_2.price)
    # print(product_2.quantity)

    print(product + product_2)
