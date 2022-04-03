import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, point):
        return math.sqrt((point.x - self.x)**2 + (point.y - self.y)**2)

    # static methods can be treated as regular external function
    # the point of having them as static methods is to have all the logically related code in one place
    # static methods have no access to `self`
    @staticmethod
    def calc_distance(point_1, point_2):
        return math.sqrt((point_1.x - point_2.x) ** 2 + (point_1.y - point_2.y) ** 2)


p = Point(5, 6)
p2 = Point(3, 4)
p.calculate_distance(p2)

# static methods are always called via the class
Point.calc_distance(p, p2)