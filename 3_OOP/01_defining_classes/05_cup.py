
'''
Create a class called Cup. Upon initialization it should receive size and quantity
(a number representing how much liquid is in it).
The class should also have a method called fill(milliliters), which will
increase the amount of liquid in the cup with the given milliliters
(if there is space in the cup, otherwise ignore).
The cup should also have a status() method which will return the amount of free
space left in the cup.

 '''
class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    # method
    def fill(self, milimeters):
        if self.quantity < self.size:
            self.quantity += milimeters
        return self.quantity

    # method
    def status(self):
        space = self.size - self.quantity
        return space

cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())
