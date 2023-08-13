
# OOP principles

* relies on the concept of classes and objects
* a class is used to create individual instance of an object

🖥️ Labs
-------------

* **Doncho**

> [https://softuni.bg/trainings/resources/video/51072/video-29-june-2020-doncho-minkov-python-oop-june-2020/2841](https://softuni.bg/trainings/resources/video/51072/video-29-june-2020-doncho-minkov-python-oop-june-2020/2841)

* **Ines**

> [https://softuni.bg/trainings/resources/video/51194/video-30-june-2020-isen-ivanova-python-oop-june-2020/2841](https://softuni.bg/trainings/resources/video/51194/video-30-june-2020-isen-ivanova-python-oop-june-2020/2841)

---

## Advantages of OOP

- provides a clear program structure **and a clean code**

* **reduces code complexity and improves readability**

* easier to maintain (i.e. a change only needs to be made at one place)

* **makes it easier to debug**

* code is **re-usable**

* could test each behaviour of an object separately

---

## Rules of thumb

* **Splitting code into functions and classes:**

  * improves readability
  * allows for easier debugging

* **A single class method should complete a single task**

```python

# bad practice
do_magic ( … )
deposit_or_withdraw ( … )
deposit_and_get_balance ( … )
parse_data_and_return_result ( … )

# best practice
withdraw ( … )
deposit ( … )
getBalance ( … )
toString ( … )
```

**The class method should clearly state what it does**

✅ By giving relevant names to functions and classes, you ensure self-documenting code

---

## What is the difference between a class and a function?

* **the class retains a `state` for itself**
* and every class execution may be different depending on the `state`

* `state`
  * helps to distinguish an object from other objects
    * a phone could have `colour`, `size` and `weight`

* `behaviour`
  * the tasks that an object performs
    * a phone could turn on or off

```python
class Phone:
    # state
    def __init__(self, color, size):
        self.color = color
        self.size = size

    # behaviour
    def turn_on(self):
        return 'The phone is turned on'
```

## What are classes?

Classes provide means of building data functionality together

* ✅ Classes allows us to **create objects that follow a certain template**
  * 💡 List is a class, Set is a class

* ➡️ Class attributes **preserve the state** 🔻
  * i.e. each class instance can have attributes for maintaining its state

  * class instance can also have methods for modifying its state

### What is an instance?

* specific realization of an object of a certain class

* The creation of an instance is called `instantiation`

  * i.e. when a class defines an `__init__()` method, this method is invoked for the newly-created class instance

```python
class Laptop:
    def __init__(self, name, model):    # class method
        self.name = name
        self.model = model              # instance attribute

my_laptop = Laptop("Inspiron 15", "Dell")
```

* `self` is used to represent the instance of a class
* `self` must always be given as the first parameter 
* `self` preserves the state of the object 
* `self` enables the class to access its own state
* `self` binds the attributes with the given arguments

```python
# example 
class Person:
    def __init__(self, name):
        print(f'Init method for person {name}')
        self.name = name
        print(self)

    def say_hello(self):
        print(f'{self.name} says "Hello"')

p = Person('Pesho')
print(p.name)
p.say_hello()

g = Person('Gosho')
print(g.name)
g.say_hello()
```

```text
Init method for person Pesho
<__main__.Person object at 0x102835ac0>
Pesho
Pesho says "Hello"
Init method for person Gosho
<__main__.Person object at 0x102a8a460>
Gosho
Gosho says "Hello"
```

#### Problem: Class Book

* create a class called `Book`
* Upon initialization it should receive:
  * `name`
  * `author`
  * `pages`

* **a Class can call another class**

```python
class Author:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def open(self):
        print(f'Opening the book {self.title} with author {self.author.first_name}')

    def close(self):
        pass

author = Author("Jay", "Shetty")      # create an object based on the class
book = Book("My Book", author, 200)   
print(book.title)
print(book.author)
print(book.pages)
print(book.author.first_name)
print(book.author.last_name)
print(book.open())
```

### Class Methods

* we define the behaviour of an object using `methods`
* A method is a `function` that works only within a `class`

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def sleep(self):
        return "sleeping.."

animal = Animal("cat")  # create an object based on the class
print(animal.sleep())   # sleeping...
```

### Using a Class

* this means creating new instances of an object and executing operation on the instances
  * **Each object** that was created based on a given class **will have a unique id**

```python
class Person():
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def eat(self):
        return 'eating...'

person = Person('Angelina', 35)

print( f'{person.name} is {person.eat()}')

# Angelina is eating...
```

### Problems

###### Car

* create a class `Car` that receives: `name`, `model`, `engine` upon initialization
* it should have a method called `get_info()` which returns `This is {name} {model} with engine {engine}`

<https://github.com/ateneva/softuni_proj/blob/main/3_OOP/01_defining_classes/ex_01_car.py>

###### Music

* create a class `Music` that receives `title`, `artist` and `lyrics` upon initialization
* it should have 2 methods:
  * `print_info()` - returns `This is {title} from {artist}`
  * `play()` - returns the lyrics

<https://github.com/ateneva/softuni_proj/blob/main/3_OOP/01_defining_classes/04_music.py>

### Data classes - as of Python 3.7

* a data class comes with basic functionality that has already been implemented

```python
from dataclasses import dataclass

@dataclass
class DataClassCard:
    rank: str
    suit: str
```

VS.

```python
class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
```

* add default values for your Data Class  

```python
from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0
```

* add methods to your data class

```python
from dataclasses import dataclass
from math import asin, cos, radians, sin, sqrt

@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

    def distance_to(self, other):
        r = 6371  # Earth radius in kilometers
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (sin((phi_2 - phi_1) / 2)**2
             + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2)**2)
        return 2 * r * asin(sqrt(h))


oslo = Position('Oslo', 10.8, 59.9)
vancouver = Position('Vancouver', -123.1, 49.3)
print(oslo.distance_to(vancouver)) #7181.7841229421165
```

### Scope & Namespace

* built-in names for example `abs()` function
  * global names in module
    * local names on function invocation

**What is a scope?**

* A region in a program where a namespace is directly accessible
  * innermost scope is searched first
    * the scopes of any enclosing functions
      * module's global names
        * built-in names

```python
def scopes():
    def local_scope():      # local scope
        text = "local text"

    def nonlocal_scope():   # non-local scope
        nonlocal text
        text = "nonlocal text"

    def global_scope():
        global text
        text = "global text"

    text = "Initial"
    print(text)

    local_scope()
    print(text)

    nonlocal_scope()
    print(text)

    global_scope()
    print(text)

scopes()
print(text)
```

```text
Initial
Initial
nonlocal text
nonlocal text
global text
```

**Problem: Scope Mess**

* Fix the provided code, so that it prints the result as expected

```
expected output:
global 
outer: local
inner: nonlocal
outer: nonlocal
global: changed!
```

```python
def outer():
    x = "local"

    def inner():
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()

print(x)
outer()
print(x)
```

⬆️ code above is confusing and unreadable and difficult to track the variable change

‼️ **Avoid using global and nonlocal**
* global variables are difficult ot track

⬇️ neater solution

```python
x = "global"

def outer():
    def inner():
        new_x = f"nonlocal{x}"
        print("inner:", new_x)
        return new_x

    def change_global():
        return "global: changed!"

    x = "local"
    print("outer:", x)
    x = inner()
    print("outer:", x)
    return change_global()


print(x)
x = outer()
print(x)
```

## The Class Object

* support two kinds of operations:
  * attribute references
    * uses standard syntax
    * valid attribute names are the ones in the class namespace

```python
class MyClass:
    "A sample example class"
    i = 12345
    
    def f(self):
        return 'hello world'
```

* instantiation
  * creates a new instance of the class and assigns this object to the local variable `x`
  * the instantiation creates an empty object
  * many classes create objects with instances customized to a specific initial state
  * therefore a class may define a special method `__init__()`

```python
class Music:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    # method
    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    # method
    def play(self):
        return self.lyrics

song = Music("Title", "Artist", "Lyrics")
print(song.print_info())
print(song.play())
```
  
* * *

Further Reading
===============

###### **Python Type Checking (Guide) – Real Python**

In this guide, you'll look at Python type checking. Traditionally, types have been handled by the Python interpreter in a flexible but implicit way. Recent versions of Python allow you to specify explicit type hints that can be used by different tools to help you develop your code more efficiently.

(<https://realpython.com/python-type-checking/>)

###### **Data Classes in Python 3.7+ (Guide) – Real Python**

Data classes are one of the new features of Python 3.7. 
With data classes you do not have to write boilerplate code to get
proper initialization, representation and comparisons for your objects.

<https://realpython.com/python-data-classes/>


###### **Why Should you Use Dataclases**

- **Less boilerplate code**


- **More readability**


- **Better code maintainability**

<https://towardsdatascience.com/9-reasons-why-you-should-start-using-python-dataclasses-98271adadc66>


