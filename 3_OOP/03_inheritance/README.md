# The Four Basic Principles of OOP
* **Inheritance**
  * extend the functionality of the code's classes to eliminate repetitive code
  

* **Encapsulation**
  * stop objects from interacting with each other so classes cannot change or interact with the specific variables 
  and functions of and object


* **Abstraction**
  * isolate impact of changes made to the code, so they only affect the variables shown and not outside code


* **Polymorphism**
  * allows different classes to have methods with the same name

--------

# Inheritance

* the capability of one class to inherit the methods and properties from another class

## Benefits of Inheritance
* code re-usability
* adds features to a class without modifying it
* it's transitive in nature

###### Example

```python
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Student(Person):
    def get_full_name(self):
        return "from student"

student = Student("John", "Smith")
print(student.get_full_name())      # from student
print(student.first_name)           # John
print(student.__repr__)             # from object
```
* **if you define a method that has exactly the same name in the child class**,
  * Python will return its values over the ones from the method of the parent class

This is because scopes in python **go from local to non-local to object**

**Once a match is found, the search stops**

----

### The `super` Method
* built-in method, which returns a temporary object of the superclass
* allows calling methods of the superclass in a subclass
* refers to the first `parent` class
* The primary use of this method is to extend the functionality of the inherited method

###### Example: Car
https://github.com/ateneva/softuni_proj/blob/main/3_OOP/03_inheritance/demo_sport_car.py

```python
class Car:
    def __init__(self, model = "Audi"):
        self.model = model
        self.gadgets = []
        
class SportCar(Car):
    def __init__(self, nick_name):
        super().__init__()              # default init without any parameters
        self.nick_name = nick_name
        
sport_car = SportCar("really fast and furious car")
a = 5
```

```python
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
print(employee.name)                # My name
print(employee.commission)          # throws AttributeError exception
```

**NOTE** child classes know the attributes of their parents but not vice versa
```
Traceback (most recent call last):
  File "/Users/angelina.teneva/Documents/GitHub/softuni_proj/3_OOP/03_inheritance/demo_person.py", line 23, in <module>
    print(employee.commission)
AttributeError: 'Employee' object has no attribute 'commission'
```

--------

## Forms of Inheritance
* `Single`       - when a `child` inherits properties from a `single parent`
* `Multiple`     - when a `child` inherits from more than 1 `parent` class
* `Multilevel`   - when a `child` class becomes a parent for another `child` class
* `Hierarchical` - when more than 1 `child` classes are created from a single `parent` class
* `Hybrid`       - consists of multiple types of inheritance

--------

### Single Inheritance
* when a `child` inherits properties from a `single parent` class only

```python
class Parent:
    def say_hi(self):
        return "Hello!"

class Child(Parent):
    def go_school(self):
        return "I go to school"

child = Child()
print(child.say_hi())       # Hello!
print(child.go_to_school)   # I go to school
```

###### Example: Student
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'{self.name} is {self.age} years old'

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_id(self):
        return self.student_id

person = Person("John", 25)
print(person.get_info())    # John is 25 years old

student = Student("Leo", 20, 10035464)
print(student.get_info())   # Leo is 20 years old
print(student.get_id())     # 10035464
```

###### Example: Animal
In a folder called project create two files: animal.py and dog.py:
* In the `animal.py` file, create a class called `Animal` with a single method `eat()` that returns: `"eating…"`. 
* In the `dog.py` file, create a class called `Dog` with a single method `bark()` that returns: `"barking…"`.
The `Dog` should inherit from `Animal`.

```python
class Animal:
    def eat(self):
        return "eating..."

class Dog(Animal):
    def bark(self):
        return "barking..."

dog = Dog()
print(dog.eat())
print(dog.bark())
```

###### Example: Food
In a folder called project create two files: food.py and fruit.py:
* In the `food.py` file, create a class called `Food` which will receive an `expiration_date` (str) upon initialization.


* In the `fruit.py` file, create a class called Fruit with will receive a `name` (str) and an expiration_date (str) upon initialization. 

* `Fruit` should inherit from `Food`.

https://github.com/ateneva/softuni_proj/tree/main/3_OOP/03_inheritance/01_food

-----

### Multiple Inheritance
* when a `child` inherits from more than 1 `parent` class
* allows modelling of complex relationships

###### Example:
```python
class Father:
    def __init__(self):
        self.father_name = "Taylor Evans"

    def say_name(self):
        return self.father_name

class Mother:
    def __init__(self):
        self.mother_name = "Bet Williams"

    def say_name(self):
        return self.mother_name

class Daughter(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)

    def get_parent_info(self):
        return f'Father: {self.father_name}, Mother: {self.mother_name}'

child = Daughter()
print(child.get_parent_info())
print(child.say_name())
```
* **NOTE**: we do not use `super` because by default it refers to the first specified class e.g. in this case `Father`

  * If we switch the place of `Father` and `Mother`, e.g. `class Daughter(Mother, Father)`
    `super` will refer to to `Mohter`


* **NOTE**: if the two parent classes have methods called in the exact name way, 
  calling the said method from the child class **will return the info from the class that has been specified first**


* **NOTE**: python assigns priority of searching for methods in the parent classes from `LEFT` to `RIGHT`
  * e.g. first in `Father`. then in `Mother`, etc.

```
Father: Taylor Evans, Mother: Bet Williams
Taylor Evans
```

-----

### Multilevel Inheritance
* when a `child` class becomes a parent for another `child` class
* Python supports `multi-level` inheritance at any depth

###### Example:
```python
class Parent:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def get_age(self):
        return self.age

class GrandChild(Child):
    def __init__(self, name, age, address):
        super().__init__(name, age)
        self.address = address

grand_child = GrandChild("Grand Name", 19, "Badema-4-A-11")
print(grand_child.name)         # Grand Name
print(grand_child.age)          # 19
print(grand_child.address)      # Badema-4-A-11
```

```python
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
```

-----------

### Hierarchical inheritance
```python
class Parent:
  def __init__(self, name):
    self.name = name

  def my_name(self):
      return self.name

  def say_hi(self):
    return f"Hi! I am {self.name}"


class Daughter(Parent):
  def __init__(self, name):
    super().__init__(name)

  def relation(self):
    return f"I am {Parent.my_name(p)}'s daughter"


class Son(Parent):
 def __init__(self, name):
      super().__init__(name)

 def relation(self):
    return f"I am my {Parent.my_name(p)}'s son"

p = Parent("Diana")
d = Daughter('Annie')
s = Son('Rossen')
print(p.say_hi())

print(d.say_hi())
print(d.relation())

print(s.say_hi())
print(s.relation())
```

---------

### MRO (Method Order Resolution)
* it is the **order in which methods should be inherited** in the presence of `multiple inheritance`
* it is possible to see MRO of a class using `mro()` method of the class

```python
class Parent:
    pass

class FirstChild(Parent):
    pass

class SecondChild(Parent):
    pass

class GrandChild(SecondChild, FirstChild):
    pass

class GrandChildTwo(FirstChild, SecondChild):
    pass

print(GrandChild.mro())
print(GrandChildTwo.mro())
```

```
[<class '__main__.GrandChild'>, <class '__main__.SecondChild'>, <class '__main__.FirstChild'>, <class '__main__.Parent'>, <class 'object'>]
[<class '__main__.GrandChildTwo'>, <class '__main__.FirstChild'>, <class '__main__.SecondChild'>, <class '__main__.Parent'>, <class 'object'>]
```

----