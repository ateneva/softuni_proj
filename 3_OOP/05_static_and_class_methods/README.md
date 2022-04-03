
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