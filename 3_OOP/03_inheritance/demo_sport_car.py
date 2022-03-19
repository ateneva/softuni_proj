
class Car:
    def __init__(self, model = "Audi"):
        self.model = model
        self.gadgets = []
        
class SportCar(Car):
    def __init__(self, nick_name):
        super().__init__()
        self.nick_name = nick_name
        
sport_car = SportCar("really fast and furious car")
a = 5