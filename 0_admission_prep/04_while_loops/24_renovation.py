
 # ************************* 04.renovation (while loop) ************************

import math as m

height = int(input())
width = int(input())
excluded = int(input())
paint = input()         # all input is defined as string and then converted to integer
total_area = height * width * 4 * (1-excluded/100)

# program should end on input = "Tired!" or when all surface has been painted
while not paint == 'Tired!':
    paint = int(paint)
    total_area -= paint

    if total_area < 0:
        print(f"All walls are painted and you have {m.floor(abs(total_area))} l paint left!")
        break

    elif total_area == 0:
        print(f"All walls are painted! Great job, Pesho!")
        break

    paint = input()    # add a string input to make sure the loop ends

else:
    print(f"{m.floor(total_area)} quadratic m left.")
