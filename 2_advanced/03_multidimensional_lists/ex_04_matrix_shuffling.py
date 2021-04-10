
'''
Write a program that reads a string, matrix, from the console and perform certain operations with its elements.
User input is provided in a similar way like in the problems above - first you read the dimensions and then the data.
Your program should receive commands in format:
    "swap row1 col1 row2 col2" where row1, row2, col1, col2 are coordinates in the matrix.
    For a command to be valid,
        it should start with the "swap" keyword
        along with four valid coordinates (no more, no less).
        You should swap the values at the given and print the matrix at each step

    If the command is not valid (doesn't contain the keyword "swap",
        has fewer or more coordinates entered
        or the given coordinates do not exist),
    print "Invalid input!" and move on to the next command.
    Your program should finish when the string "END" is entered.
'''

def read_matrix(nums):
    dimensions = [int(i) for i in nums.split()]
    rows = dimensions[0]
    matrix = []

    for _ in range(rows):
        row = input().split()
        matrix.append(row)

    return matrix

matrix = read_matrix(input())
# print(matrix)

rows_count = len(matrix)
columns_count = len(matrix[0])
matrix_size = rows_count * columns_count
# print(rows_count, columns_count)

# modify the original matrix
initial_input = input()

while initial_input != 'END':
    inputs = initial_input.split()
    element = inputs[0]

    if element == 'swap' and len(inputs) == 5:
        command = [int(i) for i in inputs[1:]]

        if min(command) > matrix_size:
            print('Invalid input!')
        else:
            # print(command)
            row1 = command[0]
            col1 = command[1]
            row2 = command[2]
            col2 = command[3]

            initial_args = matrix[row1][col1]
            updated_args = matrix[row2][col2]
            matrix[row1][col1] = updated_args
            matrix[row2][col2] = initial_args
            for sub in matrix:
                sub_format = " ".join(sub)
                print(sub_format)
    else:
        print('Invalid input!')

    initial_input = input()
