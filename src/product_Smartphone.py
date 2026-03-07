from src.product import Product


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


    def __add__(self, other):
        if type(other) is Smartphone:
            return self.quantity*self._price + other.quantity*other._price
        raise TypeError

if __name__ == "__main__":
    smartphone = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                         "S23 Ultra", 256, "Серый")

    print(smartphone.name)
    print(smartphone.description)
    print(smartphone.price)
    print(smartphone.quantity)

    print(smartphone.efficiency)
    print(smartphone.model)
    print(smartphone.memory)
    print(smartphone.color)

    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

    print (smartphone + smartphone2)