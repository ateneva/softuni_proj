from math import pi

type_of_figure = input()

if type_of_figure == "square":
    a = float(input())
    print(f"{(a * a):.3f}")
elif type_of_figure == "rectangle":
    a = float(input())
    b = float(input())
    print(f"{(a * b):.3f}")
elif type_of_figure == "circle":
    r = float(input())
    print(f"{(pi * r * r):.3f}")
else:
    a = float(input())
    h = float(input())
    print(f"{((a * h) / 2):.3f}")
