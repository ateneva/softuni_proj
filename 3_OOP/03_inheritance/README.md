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