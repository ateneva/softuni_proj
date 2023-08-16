from dataclasses import dataclass


@dataclass
class Cup:
    size: int
    quantity: int

    def status(self):
        space = self.size - self.quantity
        return space

    # methods within a class can refer to each other
    def fill(self, litres):
        if self.status() > 0:
            self.quantity += litres
        return self.quantity


cup = Cup(100, 50)
print(cup.status())
cup.fill(50)
cup.fill(10)
print(cup.status())