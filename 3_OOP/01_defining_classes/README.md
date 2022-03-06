
🖥️ Labs
-------------

*   **Doncho**

> [https://softuni.bg/trainings/resources/video/51072/video-29-june-2020-doncho-minkov-python-oop-june-2020/2841](https://softuni.bg/trainings/resources/video/51072/video-29-june-2020-doncho-minkov-python-oop-june-2020/2841)


*   **Ines**

> [https://softuni.bg/trainings/resources/video/51194/video-30-june-2020-isen-ivanova-python-oop-june-2020/2841](https://softuni.bg/trainings/resources/video/51194/video-30-june-2020-isen-ivanova-python-oop-june-2020/2841)

### OOP principles

**Splitting code into functions and classes to:** 
* improve readability
* allow for easier debugging


### Rules of thumb: 
‼️ A single class method should complete a single task

‼️ The class method should clearly state what it does

✅ By giving relevant names to functions and classes, you ensure self-documenting code



### What is the difference between a class and a function?

‼️ The difference between a function and a class is that 
* **the class retains a state for itself** 
* and every class execution may be different depending on the state

  
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

### What are classes?:
Classes create new types of objects that allow instances of that type to be made:
* ✅ Classes allows us to **create objects that follow a certain template**
  * 💡 List is a class, Set is a class

* ➡️ Class attributes **preserve the state** 🔻
  * i.e. each class instance can have attributes for maintaining its state
  * class instance can also have methods for modifying its state

```python
class Laptop:
    def __init__(self, name, model):    # class method
        self.name = name
        self.model = model              # instance attribute

my_laptop = Laptop("Inspiron 15", "Dell")
```
  * `self` is used to represent the instance of a class
  * `self` ⚠️ self must always be given as the first parameter  
  * `self` ➡️ self enables the class to access its own state
  * `self` binds the attributes with the given arguments


**Problem: Class Book**
* create a class called `Book`
* Upon initialization it should receive:
  * `name`
  * `author`
  * `pages`

```python
class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)
```

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
```

### Scope & Namespace
* built-in names for example `abs()` function
  * global names in module
    * local names on function invocation
    
**What is a scope?** 
* A region in a program where a namespace is directly accessible
  * innermost scope is searched first
    * the scopes of any enclosing fuctions
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
```

**Problem: Scope Mess**
* Fix the provided code, so that it prints the result as expected

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

‼️ **Avoid using global and nonlocal like that**

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

## The Class Object:
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

###### **Data Classes in Python 3.7+ (Guide) – Real Python**

Data classes are one of the new features of Python 3.7. With data classes you do not have to write boilerplate code to get proper initialization, representation and comparisons for your objects.

https://realpython.com/python-data-classes/

###### **Python Type Checking (Guide) – Real Python**

In this guide, you'll look at Python type checking. Traditionally, types have been handled by the Python interpreter in a flexible but implicit way. Recent versions of Python allow you to specify explicit type hints that can be used by different tools to help you develop your code more efficiently.

(https://realpython.com/python-type-checking/)