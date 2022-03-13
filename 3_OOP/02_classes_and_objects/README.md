## Instantiation
* It is known as "calling" the class
  * creates an empty object - new instance of the class
  * assings the object to a local variable

```python
class Person: 
    name = "George"
    age = 25

person = Person()
print(person.name)  # George
print(person.age)   # 25
```

* `__init__` is a magic method that creates **objects with instances, customized to a specific initial state**
  * the initial state is authomatically invoked for the newly created class instance

```python
class Laptop:
    def __init__(self, name, model):
        self.name = name
        self.model = model

my_laptop = Laptop("Inspiron 15", "Dell")
```
* the `self` parameter is used to represent the instance of the class
* it binds the attributes with the given arguments
* it is NOT a keyword, but using it increases the readability of the code

**Problem: Vehicle** 
* Create a class called `Vehicle`
  * Upon initialization, it should receive `max_speed` and `mileage`
  * The `max_speed` should be a default argument = 150
  * Create an instance called `gadgets` that is an empty list

https://github.com/ateneva/softuni_proj/blob/main/3_OOP/02_classes_and_objects/01_vehicle.py

## Attributes
* Attributes are **data** and **procedures** that belong to a class
* Valid attribute names are the ones in the class's namespace
* There are two kind of attributes references:
  * methods
  * data attributes

## Methods
* **Instance Methods**
  * define the **behaviour** of the object
  * the instance object is passed as first argument of the methods using `self` by convention

```python
class MyClass:
    def say_hello(self):
        return 'Hello'

x = MyClass()
x.say_hello()           # conventional way
MyClass.say_hello(x)    # full way
```
* **Special/Dunder Methods**
  * built-in methods that you can define to add "magic" to your classes
  * surrounded by double underscores - e.g. ``__init__``
  * enrich the class design and enhance its readability
  
```python
class Dog:
    def __init__(self, name):
        self.name = name

x = Dog("Max")
print(x.__dict__)   # {"name": "Max"}
```

* **Methods**
  * we could **change the state** of hte object using methods

```python
class Dog:
    def __init__(self, name):
        self.name = name 

    def change_name(self, new_name):
        self.name = new_name

x = Dog("Max")
x.change_name("Rex")
print(x.name)       # Rex
```

* **Common Dunder Methods:**
  * `__str__()` - returns a printable string representation of any user defined class
  * `__repr__()` - returns a machine readable representation of any user defined class

```python
class MyClass:
    def __str__(self):
        return 'This is My Class'

my_instance = MyClass()

print(str(my_instance))         # This is My Class
print(my_instance.__str__())    # This is My CLass
print(my_instance)
```
**Problem: Point**
https://github.com/ateneva/softuni_proj/blob/main/3_OOP/02_classes_and_objects/02_point.py

## Data Attributes
* values, which are **stored internally and are unique to the object**
* they define the **state** of the object

* There are **2 types of data attributes**: 
  * `instance` variables
  * `class` variable

### Instance variables vs. class variables

* `instance` variables are **UNIQUE** to each instance
* `class` variables are **shared by all instances** of the class

```python
class Laptop:
    brand = "Dell"            # class variable

    def __init__(self, name):
        self.name = name      # instance variable

first_laptop = Laptop("Latitude 5300")
second_laptop = Laptop("Inspiron 15")
print(first_laptop.brand == second_laptop.brand)  # True 
print(first_laptop.name == second_laptop.name)    # False 
```

###### BAD PRACTICE
* declare or remove data attributes outside the class
```python
class Laptop:
    def __init__(self, model):
        self.model = model

my_laptop = Laptop("Swift")

my_laptop.ram = 8
Laptop.brand = "Dell"
del my_laptop.model
```

* `instance` variables are **INDEPENDENT** from one instance to another
**NB!** modifying a `class` variable **AFFECTS all instances** at the same time

```python
class Dog:
    tricks = []                 # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

poodle = Dog("Bella")
beagle = Dog("Max")
poodle.tricks.append('roll over')
print(beagle.tricks)            # shared by all dogs ['roll over']
```

###### GOOD PRACTICE

```python
class Dog:
    kind = 'canine'             # class variable shared by all instances
    
    def __init__(self, name):
        self.name = name
        self.tricks = []        # creates empty list for each dog

poodle = Dog("Bella")
beagle = Dog("Max")
print(poodle.name, poodle.kind) # Bella canine
print(beagle.name, beagle.kind) # Max canine
poodle.tricks.append('roll over')
beagle.tricks.append('play dead')
print(poodle.tricks)            # ['roll over']
print(beagle.tricks)            # ['play dead']
```

**Problem: Circle**
https://github.com/ateneva/softuni_proj/blob/main/3_OOP/02_classes_and_objects/03_circle.py

**Problem: Glass**
https://github.com/ateneva/softuni_proj/blob/main/3_OOP/02_classes_and_objects/04_glass.py

### Special Data Attributes
* `__doc__` attribute - provides the documentation of the object as a string
* `__dict__` attribute - provides a dictionary containing a module's symbol table

```python
class MyClass:
    """This is MyClass"""

    def example(self):
        """ This is the example module of MyClass"""

print(MyClass.__doc__)              # This is MyClass
print(MyClass.example.__doc__)      # This is the example module of MyClass
```

```python
class MyClass:
    class_variable = 1

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

first = MyClass(2)
second = MyClass(3)

print(MyClass.__dict__)
print(first.__dict__)       # {'instance_variable': 2}
print(second.__dict__)      # {'instance_variable': 3}
```

**Problem: Smartphone**
https://github.com/ateneva/softuni_proj/blob/main/3_OOP/02_classes_and_objects/05_smartphone.py