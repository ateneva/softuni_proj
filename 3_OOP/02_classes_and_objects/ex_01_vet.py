'''
Create a class called Vet. Upon initialization, it should receive a name (string). It should also have an instance attribute called animals (empty list by default). There should also be 2 class attributes: animals (empty list) which will store the total amount of animals for all vets; and space (5 by default). You should create 3 additional instance methods:
-	register_animal(animal_name)
    - If there is space in the vet clinic, adds the animal to both animals' lists and returns a message: "{name} registered in the clinic"
    - Otherwise, returns "Not enough space"
-	unregister_animal(animal_name)
    - If the animal is in the clinic, removes it from both animals' lists and returns "{animal} unregistered successfully"
    - Otherwise, returns "{animal} not in the clinic"
-	info()
    - Returns info about the vet, the number of animals in his list and the free space in the clinic:
"{vet_name} has {number_animals} animals. {space_left_in_clinic} space left in clinic"

'''

class Vet:
    animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []
        # be careful where you register the empty list for the instance attribute
        # self.animals = animals will default to the class variable, not the instance variable
        # it is a VERY BAD practice to declare mutable arguments as DEFAULT in the constructor
        # https://softuni.bg/trainings/resources/video/69754/video-25-february-2022-ines-kenova-python-oop-february-2022/3591

    def register_animal(self, animal_name: str):
        if len(Vet.animals) < Vet.space:            # how to refer to a class variable
            self.animals.append(animal_name)        # add to personal vet register
            Vet.animals.append(animal_name)         # add to the clinic - e.g. registrations for all vets
            return f"{animal_name} registered in the clinic"
        else:
            return "Not enough space"

    def unregister_animal(self, animal_name: str):  # define expected input type
        if animal_name in self.animals:
            self.animals.remove(animal_name)
            Vet.animals.remove(animal_name)
            return f"{animal_name} unregistered successfully"
        else:
            return f"{animal_name} not in the clinic"

    def info(self):
        vet_name = self.name
        number_animals = len(self.animals)
        space_left_in_clinic = Vet.space - len(Vet.animals)
        return f'"{vet_name} has {number_animals} animals. {space_left_in_clinic} space left in clinic"'

peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
