
# *********** 02.Easter Guests (conditional statements) ************************

import math as m

guests = int(input())
budget = int(input())

pastry = m.ceil(guests / 3)
eggs = guests * 2

total = pastry * 4 + eggs * 0.45
left = abs(budget - total)

if total <= budget:
    print(f"Lyubo bought {pastry} Easter bread and {eggs} eggs.")
    print(f"He has {left:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {left:.2f} lv. more.")
