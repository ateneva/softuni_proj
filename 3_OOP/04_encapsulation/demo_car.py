class Car:
    def __init__(self):
        self.__max_speed = 200

    def drive(self):
        print('driving max speed ' + str(self.__max_speed))


red_car = Car()
red_car.drive()             # driving max speed 200
red_car.__max_speed = 10    # won't change because it is name mangled
red_car.drive()             # driving max speed 200

# double check behaviour in debug mode
red_car.max_speed = 10    # adds a new public attribute which is different than the  one in th class
print(red_car.max_speed)  # max_speed = 10
print(red_car.drive())    # driving max speed 200
