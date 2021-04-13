
'''
We receive the size of the field in which our miner moves.
The field is always a square. After that, we will receive the commands,
which represent the directions, in which the miner should move.
    The miner starts from position - 's'.
    The commands will be: left, right, up and down.
    If the miner has reached the edge of the field and the next command indicates
    that he has to get out of the field, he must remain on his current possition
        and ignore the current command.

    The possible characters that may appear on the screen are:
    -  * -> a regular position on the field.
    -  e -> the end of the route.
    -  c -> coal
    -  s -> the place where the miner starts

When the miner finds a coal, he collects it and replaces it with '*'.
Keep track of the count of the collected coals.

If the miner collects all of the coals in the field, the program stops
    and you have to print the following message: "You collected all coals! ({rowIndex}, {colIndex})".

If the miner steps at 'e', the game is over (the program stops)
    and you have to print the following message: "Game over! ({rowIndex}, {colIndex})".

If there are no more commands and none of the above cases had happened,
    you have to print the following message: "{remainingCoals} coals left. ({rowIndex}, {colIndex})".

'''

from collections import deque

def get_matrix(size):
    matrix = []
    for _ in range(size):
        matrix_line = [x for x in input().split()]
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
        print(f)
        for position in f:
            if position == 's':
                initial_position = [field.index(f), f.index(position)]

    return initial_position


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


def available_coal(field):
    coal = sum([f.count("c") for f in field])
    return coal

################################################################################

n = int(input())
directions = deque(input().split())

final_position = []
collected_coals = 0
game_over = False
all_collected = False

# get matrix
field = get_matrix(n)

# determine initial position and available coal
starting_position = get_initial_position(field)
all_coal = available_coal(field)

print(f'Initial position is {starting_position}; available coal is {all_coal}')

while directions:
    direct = directions.popleft()
    new_row = 0
    new_col = 0
    position = get_new_position(starting_position, new_row, new_col, direct)

    # if new position is not valid,
    # remain on current position and ignore the current command
    if is_valid(position, n):
        final_position.insert(0, position)
        starting_position = position  # reset initial position for next run

        # devise item collection logic
        field_value = field[position[0]][position[1]]

        if field_value == 'e':
            game_over = True
            break

        elif field_value == 'c':
            field[position[0]][position[1]] = '*'
            collected_coals += 1

            if collected_coals == all_coal:
                all_collected = True
                break

last_position = tuple(final_position[0])
coal_left = all_coal - collected_coals

if game_over:
    print(f'Game over! {last_position}')

elif all_collected:
    print(f'You collected all coals! {last_position}')

else:
    print(f'{coal_left} coals left. {last_position}')
