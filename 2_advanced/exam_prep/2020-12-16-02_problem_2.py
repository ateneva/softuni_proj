
'''
You will be given a string. Then, you will be given an integer N for the size of the field with square shape.
On the next N lines, you will receive the rows of the field.

The player will be placed on a random position, marked with "P".
On random positions there will be letters.
All of the empty positions will be marked with "-".

Each turn you will be given commands for the player’s movement.
If he moves to a letter, he consumes it, concatеnates it to the initial string
and the letter disappears from the field.

If he tries to move outside of the field, he loses the last letter in the string,
    if there are any, and the player’s position is not changed.
At the end print all letters and the field.

Input
    - On the first line, you are given the initial string
    - On the second line, you are given the integer N - the size of the square matrix
    - The next N lines holds the values for every row
    - On the next line you receive a number M
    - On the next M lines you will get a move command

Output
    - On the first line the final state of the string
    - In the end print the matrix

Constraints
    - The size of the square matrix will be between [2…10]
    - The player position will be marked with "P"
    - The letters on the field will be any letter except for "P"
    - Move commands will be: "up", "down", "left", "right"

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


def get_directions(m):
    all_directions = [input() for _ in range(m)]
    return all_directions


def get_initial_position(field):
    initial_position = []
    for f in field:
        for position in f:
            if position == 'P':
                initial_position = [field.index(f), f.index(position)]
    return initial_position


def get_new_position(initial_position, row, col, direction):
    if direction == 'up':
        row = initial_position[0] - 1
        col = initial_position[1]

    elif direction == 'down':
        row = initial_position[0] + 1
        col = initial_position[1]

    elif direction == 'right':
        row = initial_position[0]
        col = initial_position[1] + 1

    elif direction == 'left':
        row = initial_position[0]
        col = initial_position[1] - 1

    new_position = [row, col]
    return new_position

####################################################################################################

initial_string = input()
final_string = initial_string.split()

# get matrix
matrix_size = int(input())
matrix = get_matrix(matrix_size)

for m in matrix:
    print(m)

# get starting position
starting_position = get_initial_position(matrix)
print(f'Initial position is {starting_position}')

# get directions
num_commands = int(input())
directions = get_directions(int(num_commands))
all_movements = []

for direction in directions:
    new_row = 0
    new_col = 0
    position = get_new_position(starting_position, new_row, new_col, direction)

    # if new position is not valid,
    # remain on current position
    if is_valid(position, matrix_size):

        # reset previous position
        matrix[starting_position[0]][starting_position[1]] = '-'

        # reset previuous position for next run
        starting_position = position

        # record movement
        all_movements.insert(0, position)

        # devise item collection logic
        field_value = matrix[position[0]][position[1]]

        if field_value != '-':
            matrix[position[0]][position[1]] = 'P'  # consume letter
            final_string.append(field_value)
    else:
        final_string.pop()

print("".join(final_string))

for mat in matrix:
    print("".join(mat))

print(f'Final position is {starting_position}')
print(all_movements)
