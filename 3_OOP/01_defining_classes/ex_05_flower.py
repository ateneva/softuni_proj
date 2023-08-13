
'''
Create a class called Flower. Upon initialization, the class should receive
name and water_requirements.

The flower should also have an attribute called
is_happy (False by default) and a method called water(quantity), which will
water the flower.

If the water is greater than or equal of the requirements of
the flower, it becomes happy. (set is_happy to True).

The last method should be called status() and it should return "{name} is happy"
if the flower is happy, otherwise it should return "{name} is not happy".
'''


class Flower:
    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False
        self.current_water = 0  # assign default attribute

    def water(self, quantity):
        self.current_water += quantity
        self.is_happy = self.check_happy_status()

    # keep rule of thumb - 1 method should do 1 thing and its name should be indicative of its behaviour
    def check_happy_status(self):
        return self.water_requirements <= self.current_water

    def status(self):
        if self.is_happy:
            return f"{self.name} is happy"
        else:
            return f"{self.name} is not happy"


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())
