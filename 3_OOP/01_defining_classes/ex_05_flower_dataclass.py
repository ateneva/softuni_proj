from dataclasses import dataclass


@dataclass
class Flower:
    # Upon initialization, the class should receive name and water_requirements
    name: str
    water_requirements: int

    # attributes
    is_happy = False
    current_water = 0

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