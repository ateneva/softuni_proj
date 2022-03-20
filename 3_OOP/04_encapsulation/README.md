
## What is Encapsulation?

* packing of data and functions into a single component

* allows putting restrictions and preventing accidental modification of data

* to do that, an object variable, can only be changed by an object method

-------------------------

## Encapsulation in Python

* everything written within the python class (methods and variables) are public by default

* Python implements weak encapsulation
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

* a name prefixed with an `underscore` should be treated as a `protectec` method, variable
  * its access outside the class is still possible in the regular way **BUT**
    * pycharm gives notification on hover that the attribute is `PROTECTED`

  * classes that inherit from the parent class are ALSO able to access `PROTECTED` attributes

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

* naming an attribute with two leading `__` underscores invokes name mangling


* Name mangling is used to show that a **variable should NOT be accessed outside the class**
  * it also makes the attribute inaccessible to its `child` classes

```python
class CreditCard:
    def __init__(self, number, expiry_date, cvv, name, pin):
        self.number = number
        self.expiry_date = expiry_date
        self._cvv = cvv         # protected attribute
        self.name = name
        self.__pin = pin        # private attribute

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            return
        raise ValueError("Old pin is not correct")

class ChildCredit(CreditCard):
    def __init__(self, number, expiry_date, cvv, name, pin, child_name):
        super().__init__(number, expiry_date, cvv, name, pin)
        self.child_name = child_name
        self._cvv = cvv

card = CreditCard(1234567891012345, "2022-10", 256, "Test Name", 7887)

# will raise an attribute error if you try to access mangled variable the usual way
print(card.__pin)
print(card.pin)

# the private variable can still be accessed by using the mangled name
# can be seen by stepping through the class in debug mode
print(card._CreditCard__pin)


# VERY BAD PRACTICE
# modifying a private variable outside the class
card.pin = 123456
print(card.pin)  # 123456
```

* Python **does not restrict access** to such mangled attributes
    * it is still possible to `access` or `modify` a variable that is considered `private` from outside the class
    * THAT, however, is considered a **VERY BAD PRACTICE**

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

red_car.max_speed = 10    # still changes to 10
print(red_car.max_speed)  # max_speed = 10
print(red_car.drive())    # driving max speed 200
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

------------------------------------------------

#### Getter and Setters (1

* the `pythonic` way of defining `getters` and `setters` is using `properties`

* BY defining `properties`, you **can change the internal implementation** of a class **without affecting the program*

* use `properties` to introduce validations within your methods

```python
class Person:
    def __init__(self, age=0):
        self.age = age
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if age < 18: self.__age = 18
        else: self.__age = age

person = Person(25)
print(person.age)	# 25
person.age = 10
print(person.age)	# 18
```

###### Example: Car

```python
class Car:
    def __init__(self, max_speed: int):
        self.max_speed = max_speed

    def drive(self):
        print('driving max speed ' + str(self.max_speed))

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, value):
        if value > 447:
            value = 447
        self.__max_speed = value

red_car = Car(200)
red_car.drive()             # driving max speed 200
red_car.max_speed = 512     # changes the speed to 447
red_car.drive()             # driving max speed 447
```

* you should use Python `properties` to **apply rules** to an attribute

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value <= 0: 
            raise Exception("Age must be greater than zero")
        self.__age = value
```

