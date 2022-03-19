class Father:
    def __init__(self):
        self.father_name = "Taylor Evans"

    def say_name(self):
        return self.father_name

class Mother:
    def __init__(self):
        self.mother_name = "Bet Williams"

    def say_name(self):
        return self.mother_name

class Daughter(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)

    def get_parent_info(self):
        return f'Father: {self.father_name}, Mother: {self.mother_name}'

child = Daughter()
print(child.get_parent_info())  # Father: Taylor Evans, Mother: Bet Williams
print(child.say_name())