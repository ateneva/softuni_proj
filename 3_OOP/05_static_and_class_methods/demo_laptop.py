
class Laptop:
    def __init__(self, memory, model):
        self.memory = memory
        self.model = model

    # create instances of the class object
    @classmethod
    def low_ram_laptop(cls, model):
        return cls(8, model)

    @classmethod
    def high_ram_laptop(cls, model):
        return cls(32, model)

    def __str__(self):
        return f'Laptop {self.model} with RAM {self.memory}'


laptop1 = Laptop.low_ram_laptop("Dell")
print(laptop1)

laptop2 = Laptop.high_ram_laptop("Mac")
print(laptop2)

laptop3 = Laptop(16, "Asus")
print(laptop3)