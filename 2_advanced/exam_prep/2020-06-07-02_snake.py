
'''
You will be given an integer n for the size of the snake territory with square shape.
On the next n lines, you will receive the rows of the territory.
The snake will be placed on a random position, marked with the letter 'S'.
On random positions there will be food, marked with '*'.
There might also be a lair on the territory. The lair has two burrows.
They are marked with the letter - 'B'.
All of the empty positions will be marked with '-'.

Each turn, you will be given command for the snake’s movement.
When the snake moves it leaves a trail marked with '.'

Move commands will be: "up", "down", "left", "right".
If the snake moves to a food, it eats the food and increases the food quantity with one.
If it goes inside of a burrow, it goes out on the position of the other burrow
    and then both burrows disappear.

If the snake goes out of its territory, it loses, can't return back and the program ends.
When the snake has gone outside of its territory or has eaten enough food, the game ends.
The snake needs at least 10 food quantity to win.

Input
    - On the first line, you are given the integer n – the size of the square matrix.
    - The next n lines holds the values for every row.
    - On each of the next lines you will get a move command.

Output
    - On the first line:
        - If the snake goes out of its territory, print: "Game over!"
        - If the snake eat enough food, print: "You won! You fed the snake."
    - On the second line print all food eaten: "Food eaten: {food quantity}"
    - In the end print the matrix.

Constraints
    - The size of the square matrix will be between [2…10].
    - There will always be 0 or 2 burrows, marked with - 'B'.
    - The snake position will be marked with 'S'.
    - The snake will always either go outside its territory or eat enough food.
    - There will be no case in which the snake will go through itself.
'''

def get_matrix(size):
    matrix = []
    for _ in range(size):
        matrix_line = [x for x in input()]
        matrix.append(matrix_line)
    return matrix

def is_valid(pos, size):
    r = pos[0]
    c = pos[1]

    # check the indexes are within bounds
    within_bounds = 0 <= r < size and 0 <= c < size
    return within_bounds


def get_initial_position(field):
    initial_position = []
    for f in field:
        for position in f:
            if position == 'S':
                initial_position = [field.index(f), f.index(position)]
    return initial_position


def get_burrows(field):
    burrows = []
    for f in field:
        for position in f:
            if position == 'B':
                burrow = [field.index(f), f.index(position)]
                burrows.append(burrow)
    return burrows


def get_new_position(initial_position, row, col, direction):
    if direction == 'up':
        row = initial_position[0] - 1
        col = initial_position[1]

    elif direction == 'right':
        row = initial_position[0]
        col = initial_position[1] + 1

    elif direction == 'down':
        row = initial_position[0] + 1
        col = initial_position[1]

    elif direction == 'left':
        row = initial_position[0]
        col = initial_position[1] - 1

    new_position = [row, col]
    return new_position

##############################################################################

out_of_bounds = False
food_eaten = 0

# get territory
territory_size = int(input())
territory = get_matrix(territory_size)

# get starting position
starting_position = get_initial_position(territory)
print(f'Initial position is {starting_position}')

# find the entry and exit to the lair if such
lair = get_burrows(territory)
if len(lair) > 0:
    first_burrow = lair[0]
    second_burrow = lair[1]
    print(f'1st burrow is {first_burrow}; 2nd burrow is {second_burrow}')

for t in territory:
    print(t)

while True:
    direct = input()
    new_row = 0
    new_col = 0
    position = get_new_position(starting_position, new_row, new_col, direct)

    if is_valid(position, territory_size):
        # leave trail on previous position
        territory[starting_position[0]][starting_position[1]] = '.'

        # reset previuous position for next run
        starting_position = position

        # devise item collection logic
        field_value = territory[position[0]][position[1]]

        if field_value == 'B':
            # eliminate burrow entry
            territory[position[0]][position[1]] = '.'

            # change position to burrow exit
            if position == first_burrow:
                starting_position = second_burrow
            else:
                starting_position = first_burrow

            # eliminate burrow exit
            territory[starting_position[0]][starting_position[1]] = 'S'

        elif field_value == '*':
            territory[position[0]][position[1]] = '.'
            food_eaten += 1

            if food_eaten == 10:
                territory[position[0]][position[1]] = 'S'  # reset snake position
                break
        else:
            territory[position[0]][position[1]] = '.'      # leave trail on empty spots

    else:
        out_of_bounds = True
        break

if out_of_bounds:
    print("Game over!")
    print(f"Food eaten: {food_eaten}")
else:
    print('You won! You fed the snake.')
    print(f"Food eaten: {food_eaten}")

for t in territory:
    print("".join(t))
