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

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"]
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = float(new_price)


if __name__ == "__main__":
    product = Product("огурец", "овощь", 56.5, 5)

    print(product.name)
    print(product.description)
    print(product.price)
    print(product.quantity)

    product_2 = Product.new_product({"name": "манго", "description": "фрукт", "price": 76.5, "quantity": 3})

    print(product_2.name)
    print(product_2.description)
    print(product_2.price)
    print(product_2.quantity)

    product_2.price = 50
    print(product_2.name)
    print(product_2.description)
    print(product_2.price)
    print(product_2.quantity)
