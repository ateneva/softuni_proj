
# Static Methods
* it knows nothing about the class or instance it is called on
* static methods have no access to `self`
* it **CANNOT** modify object or class state

```python
class Person:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def is_adult(age):
        return age >= 18

# Always call static methods through the name of the class
print(Person.is_adult(5))    # False


# Calling a static method through the instance is NOT good practice
girl = Person("Amy")
print(girl.is_adult(20))     # True
```

## Benefits of static methods

# Class Methods
* it is bound to the class and **NOT the object**
* it **can modify a class state that would apply** across all instances of the class

```python
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def pepperoni(cls):
        return cls(["tomato sauce", "parmesan", "pepperoni"])

    @classmethod    
    def quattro_formaggi(cls):
        return cls(["mozzarella", "gorgonzola", "fontina", "parmigiano"])


first_pizza = Pizza.peperoni()
second_pizza = Pizza.quattro_formaggi()
```

## Benefits of Class Methods:
* provide a shortcut **for creating new instance objects**
* ensures correct instance creation of the derived class
* You could **easily follow the `DRY` principle** (e.g. DO NOT REPEAT YOURSELF)