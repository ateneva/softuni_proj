class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, work_id, salary):
        super().__init__(name, age)
        self.work_id = work_id
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, age, work_id, salary, commission):
        super().__init__(name, age, work_id, salary)
        self.commission = commission


person = Person("Test", 30)
employee = Employee("My Name", 20, 1015, 500)
print(employee.name)
print(employee.commission)