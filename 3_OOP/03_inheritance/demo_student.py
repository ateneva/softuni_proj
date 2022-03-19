class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Student(Person):
    def get_full_name(self):
        return "from student"

# if you define a method that has exactly the same name in the child class,
# Python will return its values over the ones from the method of the parent class

# This is because scopes in python go from local to non-local to object
# Once a match is found, the search stops

# NOTE child classes know the attributes of their parents but not vice versa

student = Student("John", "Smith")
print(student.get_full_name())      # from student
print(student.first_name)           # John
print(student.__repr__)             # from object

