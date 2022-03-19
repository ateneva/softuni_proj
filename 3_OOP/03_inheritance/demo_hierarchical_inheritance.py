class Parent:
  def __init__(self, name):
    self.name = name

  def my_name(self):
      return self.name

  def say_hi(self):
    return f"Hi! I am {self.name}"


class Daughter(Parent):
  def __init__(self, name):
    super().__init__(name)

  def relation(self):
    return f"I am {Parent.my_name(p)}'s daughter"


class Son(Parent):
 def __init__(self, name):
      super().__init__(name)

 def relation(self):
    return f"I am my {Parent.my_name(p)}'s son"

p = Parent("Diana")
d = Daughter('Annie')
s = Son('Rossen')
print(p.say_hi())

print(d.say_hi())
print(d.relation())

print(s.say_hi())
print(s.relation())