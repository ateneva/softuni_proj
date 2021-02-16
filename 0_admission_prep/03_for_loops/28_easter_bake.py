
# Admission exam 2019-04-21 Easter Bake ****************************************

import math as m

pastries = int(input())
sugar = 0
flour = 0
max_sugar = -10000
max_flour = -10000

for pastry in range(pastries):
    sugar_used = int(input())        # 950 gram per packet
    flour_used = int(input())        # 750 gram per packet

    sugar += sugar_used
    flour += flour_used

    sugar_needed = m.ceil(sugar/950)
    flour_needed = m.ceil(flour/750)

    if sugar_used > max_sugar:
        max_sugar = sugar_used

    if flour_used > max_flour:
        max_flour = flour_used

print(f"Sugar: {sugar_needed}")
print(f"Flour: {flour_needed}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
