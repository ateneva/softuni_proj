
# Admission exam 2019-04-21 Easter Eggs ***************************************

eggs = int(input())
red = 0
orange = 0
blue = 0
green = 0

for egg in range(eggs):
    egg_colour = input()

    if egg_colour == 'red':
        red += 1

    elif egg_colour == 'orange':
        orange += 1

    elif egg_colour == 'blue':
        blue += 1

    elif egg_colour == 'green':
        green += 1

    max_eggs = max(red, orange, blue, green)

    if max_eggs == red:
        max_colour = "red"

    elif max_eggs == orange:
        max_colour = "orange"

    elif max_eggs == blue:
        max_colour = "blue"

    elif max_eggs == green:
        max_colour = "green"

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_eggs} -> {max_colour}")
