
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
