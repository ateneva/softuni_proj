
'''
Create a class SportsCar with a single method race() that returns: "racing..."
'''

#from project.vehicle import Vehicle
from project.car import Car

class SportsCar(Car):
    def race(self):
        return "racing..."


'''
# TO DEBUG locally
sport_car = SportsCar()
print(sport_car.move())
print(sport_car.drive())
print(sport_car.race())
'''