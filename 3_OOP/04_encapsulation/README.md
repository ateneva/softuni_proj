
## What is Encapsulation

* packing of data and functions into a single component

* allows putting restrictions and preventing accidental modification of data

* to do that, an object variable, can only be changed by an object method

-------------------------

## Encapsulation in Python

* everything written within the python class (methods and variables) are public by default

* Python imlements weak encapsulation
  * e.g. it is performed by convention rather than being enforced by language

---------------------------

## Access Modifiers

* How to control access?
  * using `single underscore`
  * using `double underscore`  - e.g. make it private
  * using `getter` and `setter` methods to access private variables

* It is a matter of convention to differentiate into 3 terms `public`, `protected` and `private`

------------------------------

### Single Underscore
+ a name prefixed with an `underscore` should be treated as a `non-public` method, variable

```python
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self._age = age

person = Person('Peter', 25)
print(person.name)	# Peter
print(person._age)	# 25
```

------------------------------

### Double Underscore

* naomg an attribute with two leading `__` underscores invokes name mangling


* Name mangling is used to show that a **variable should NOT be accessed outside the class**

* Python **does not restrict access** to such attributes
    * it is still possible to `access` or `modify` a variable that is considered `private` from outside the class

```python
class Car:
    def __init__(self):
        self.__max_speed = 200
     
    def drive(self):
        print('driving max speed ' + str(self.__max_speed))

red_car = Car()
red_car.drive()           # driving max speed 200
red_car.__max_speed = 10  # won't change because it is name mangled
red_car.drive()           # driving max speed 200
```

-------------------------------------------------

### Getter and Setter Methods

* used to access and change the `private` variables as they are part of the class

```python
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age

    def info(self):
        print(self.name)
        print(self.__age)

    def get_age(self):       # getter
        print(self.__age)

    def set_age(self, age):  # setter
        self.__age = age


person = Person('Peter', 25)
        
# accessing data using class method
person.info()	# Peter 25
        
# changing age using setter
person.set_age(26)
person.get_age()	# 26
```
