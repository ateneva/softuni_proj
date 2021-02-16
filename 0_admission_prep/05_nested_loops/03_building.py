
# building----------------------------------------------------------------------

floors = int(input())
spaces = int(input())

for i in range(floors, 0, -1):  # looping in reverse order
    for j in range(spaces):

        if floors == 1 \
                or (i % 2 == 0 and i == floors) \
                or (i % 2 != 0 and i == floors):
            print('L{0}{1} '.format(i, j), end="")  # large apartments

        elif i % 2 == 0 and i != floors:  # office
            print('O{0}{1} '.format(i, j), end="")

        elif i % 2 != 0 and i != floors:  # apartments
            print('A{0}{1} '.format(i, j), end="")

    print()  # starting on a new line
