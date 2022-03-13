'''
Create a class called Circle. Upon initialization, it should receive a radius (number). Create a class attribute called pi which should be equal to 3.14. Create 3 instance methods:
-	set_radius(new_radius) - changes the radius
-	get_area() - returns the area of the circle
-	get_circumference() - returns the circumference of the circle

'''


class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    # better clearly define that pi is a class attribute
    def get_area(self):
        area = self.radius * self.radius * Circle.pi
        return area

    def get_circumference(self):
        return 2 * Circle.pi * self.radius

circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())

# each inatance has its own radius
circle_2 = Circle(50)
print(circle.radius)    # 12
print(circle_2.radius)  # 50

# the class attribute for the two instances is the same
print(circle.pi)    # 3.14
print(circle_2.pi)  # 3.14

# UNLIKE instance attributes, class attributes can be accessed via the class as well
print(Circle.pi)        # 3.14
print(Circle.radius)    # throws attribute error