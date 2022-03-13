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
  pass

student = Student("John", "Smith")
print(student.get_full_name())
```

### The `super` Method
* built-in method, which returns a temporary object of the superclass
* allows ypou to call methods of the superclass in a subclass
* The primary use of this method is to extend the functionality of the inherited method

###### Example
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

###### Example: Food
In a folder called project create two files: food.py and fruit.py:
* In the `food.py` file, create a class called `Food` which will receive an `expiration_date` (str) upon initialization.


* In the `fruit.py` file, create a class called Fruit with will receive a `name` (str) and an expiration_date (str) upon initialization. 


* `Fruit` should inherit from `Food`.

https://github.com/ateneva/softuni_proj/tree/main/3_OOP/03_inheritance/01_food

## Forms of Inheritance
* `Single`
* `Multiple`
* `Multilevel`
* `Hierarchical`
* `Hybrid` - consists of multiple types of inheritance

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
###### Example:
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

### Multiple Inheritance
* when a `child` inherits from more than 1 `parent` class
* allows modelling of complex relationships

###### Example:
```python
class Father:
    def __init__(self):
        self.father_name = "Taylor Evans"

class Mother:
    def __init__(self):
        self.mother_name = "Bet Williams"

class Daughter(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)

    def get_parent_info(self):
        return f'Father: {self.father_name}, Mother: {self.mother_name}'

child = Daughter()
print(child.get_parent_info())  # Father: Taylor Evans, Mother: Bet Williams
```


