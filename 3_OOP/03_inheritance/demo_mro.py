class Parent:
    pass

class FirstChild(Parent):
    pass

class SecondChild(Parent):
    pass

class GrandChild(SecondChild, FirstChild):
    pass

class GrandChildTwo(FirstChild, SecondChild):
    pass

print(GrandChild.mro())
print(GrandChildTwo.mro())