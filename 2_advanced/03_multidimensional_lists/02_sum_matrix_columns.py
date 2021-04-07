
'''
Write a program that reads a matrix from the console and prints the sum for each column.
On the first line, you will get the matrix's rows.
On the next rows, you will get elements for each column separated with a space.
'''

matrix_type = input().split(', ')

rows = int(matrix_type[0])
columns = int(matrix_type[1])
matrix = []

for r in range(rows):
    row = [int(i) for i in input().split(' ')]
    matrix.append(row)


columns_sum = [0] * columns
for row in range(rows):
    for column in range(columns):
        columns_sum[column] += matrix[row][column]

for n in columns_sum:
    print(n)
