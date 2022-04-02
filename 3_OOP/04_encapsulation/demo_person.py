class Person:
    def __init__(self, age=0):
        # if the variable is declared as private the getter and setter won't be triggered on initialization
        self.age = age

        '''
        # we do not define checks in the _init__ :
        #  they are only applied during initialization and not on subsequent change attempt
        if age < 0:
            raise ValueError("Age is not valid")
        '''

    # age in the getter must be defined as private to avoid recursion
    @property
    def age(self):
        return self.__age

    # age in the setter must be defined as private to avoid recursion
    @age.setter
    def age(self, age):
        if age < 18:
            self.__age = 18
            raise Exception("Age must be greater than 18")
        self.__age = age


person = Person(25)
print(person.age)  # 25
person.age = 10
print(person.age)  # 18