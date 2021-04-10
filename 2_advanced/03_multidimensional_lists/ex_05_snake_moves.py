
'''
A snake is represented by a string.
The isle is a rectangular matrix of size NxM.
A snake starts going down from the top-left corner and slithers its way down.
    The first cell is filled with the first symbol of the snake,
    the second cell is filled with the second symbol, etc.

The snake is as long as it takes in order to fill the stairs completely
    - if you reach the end of the string representing the snake,
        start again at the beginning.
After you fill the matrix with the snake's path, you should print it.
'''

from collections import deque

def read_matrix(nums):
    dimensions = [int(i) for i in nums.split()]
    rows = dimensions[0]
    columns = dimensions[1]
    matrix = []

    for _ in range(rows):
        row = [""] * columns
        matrix.append(row)

    return matrix

matrix = read_matrix(input())
print(matrix)

snake = deque(input())
print(snake)

rows = len(matrix)
cols = len(matrix[0])

for row in range(rows):
    for col in range(cols):
        current_col = col
        current_char = snake.popleft()

        # flip columns if row is odd
        # <------
        if row % 2 != 0:
            current_col = cols - 1 - col

        # fill the empty matrix position
        matrix[row][current_col] = current_char

        # add the the current character to the enc
        snake.append(current_char)

for row in matrix:
    print("".join(row))
