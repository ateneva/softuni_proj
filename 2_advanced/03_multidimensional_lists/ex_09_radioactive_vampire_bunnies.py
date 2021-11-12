

def read_matrix(nums):
    dimensions = [int(i) for i in nums.split()]
    rows = dimensions[0]
    columns = dimensions[1]
    matrix = []

    for _ in range(rows):
        row = [x for x in input()]
        matrix.append(row)

    return matrix


def is_valid(pos, size):
    r = pos[0]
    c = pos[1]

    # check the indexes are within bounds
    within_bounds = 0 <= r < size and 0 <= c < size
    return within_bounds


def in_range(x, y, size):
    return 0 <= x < size and 0 <= y < size


def get_player_position(field):
    player_position = []
    for f in field:
        for position in f:
            if position == 'P':
                player_position = [field.index(f), f.index(position)]
    return player_position


def get_bunnies_positions(field):
    bunnies = []
    for f in field:
        for position in f:
            if position == 'B':
                bunny = [field.index(f), f.index(position)]
                bunnies.append(bunny)
    return bunnies


def get_new_position(player_position, row, col, direction):
    if direction == 'U':
        row = player_position[0] - 1
        col = player_position[1]

    elif direction == 'R':
        row = player_position[0]
        col = player_position[1] + 1

    elif direction == 'D':
        row = player_position[0] + 1
        col = player_position[1]

    elif direction == 'L':
        row = player_position[0]
        col = player_position[1] - 1

    new_position = [row, col]
    return new_position


#############################################################################

lair_size = input()
lair = read_matrix(lair_size)
directions = [d for d in input()]
rows_count = len(lair)
cols_count = len(lair[0])
lair_bounds = rows_count * cols_count

for l in lair:
    print(l)

print(directions)

starting_position = get_player_position(lair)
print(f'Player position is {starting_position}')

original_bunnies = get_bunnies_positions(lair)
print(original_bunnies)

all_movements = []

for direction in directions:

    # populate bunnies
    for bunny in original_bunnies:
        bunny_row = bunny[0]
        bunny_col = bunny[1]

        for r in range(bunny_row - 1, bunny_col + 2):
            for c in range(bunny_row - 1, bunny_col + 2):
                if in_range(r, c, lair_bounds):
                    bunny_pos = [r, c]
                    lair[bunny_row][bunny_col] = 'B'


for l in lair:
    print("".join(l))

print(f'Final position is {starting_position}')
print(all_movements)