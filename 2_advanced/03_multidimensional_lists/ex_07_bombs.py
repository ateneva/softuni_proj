
'''
You will be given a square matrix of integers, each integer
    separated by a single space, and each row on a new line.
    
Then on the last line of input you will receive
    indexes - coordinates to several cells separated by a single space,
    in the following format: row1,column1 row2,column2 row3,column3…

On those cells there are bombs. You must detonate every bomb, in the order they
were given. When a bomb explodes, it deals damage equal to its own integer value,
to all the cells around it (in every direction and in all diagonals).

One bomb can't explode more than once and after it does, its value becomes 0.
When a cell's value reaches 0 or below, it dies. Dead cells can't explode.
You must print the count of all alive cells and their sum.
Afterwards, print the matrix with all its cells (including the dead ones).
'''

def get_square_matrix(size):
    matrix = []
    for _ in range(size):
        matrix_line = [int(x) for x in input().split()]
        matrix.append(matrix_line)
    return matrix


def get_valid_coordinates(inputs):
    valid_coordinates = []
    for c in inputs.split():
        row = int(c[0])
        col = int(c[2])
        coordinates = [row, col]
        valid_coordinates.append(coordinates)
    return valid_coordinates


def in_range(x, y, size):
    return 0 <= x < size and 0 <= y < size


######################################################################
matrix_size = int(input())
matrix = get_square_matrix(matrix_size)
index_coordinates = input()
bombs = get_valid_coordinates(index_coordinates)

'''
print(bombs)

for m in matrix:
    print(m)
'''

for bomb in bombs:
    bomb_row = bomb[0]
    bomb_col = bomb[1]
    bomb_damage = matrix[bomb_row][bomb_col]

    if matrix[bomb_row][bomb_col] > 0:

        for r in range(bomb_row - 1, bomb_row + 2):
            for c in range(bomb_col - 1, bomb_col + 2):
                if in_range(r, c, matrix_size):
                    damage = [r, c]

                    # when bomb explodes it's equal to 0
                    if damage == bomb:
                        matrix[bomb_row][bomb_col] = 0

                    # damage is only dealt to positive cells
                    elif damage != bomb:
                        if matrix[r][c] > 0:
                            matrix[r][c] -= bomb_damage


#print(matrix)
active_cells = []
for m in matrix:
    for elem in m:
        if elem > 0:
            active_cells.append(elem)

print(f"Alive cells: {len(active_cells)}")
print(f"Sum: {sum(active_cells)}")

for m in matrix:
    print(" ".join([str(i) for i in m]))
