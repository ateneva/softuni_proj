
'''
Create a class called Car. Upon initialization it should receive a name,
model and engine (all strings).
Create a method called get_info() which will return a string in the following format:
    "This is {name} {model} with engine {engine}".
'''

class Car:
    def __init__(self, name: str, model: str, engine: str):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"


# create an object based on the class
car = Car("Kia", "Rio", "1.3L B3 I4")
print(car.get_info())

car_2 = Car('Audi', 'a6', "1.3L B3 I4")
print(car_2.get_info())