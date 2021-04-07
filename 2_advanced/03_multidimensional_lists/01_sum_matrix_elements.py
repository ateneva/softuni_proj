
'''
Write a program that reads a matrix from the console and prints:
    * The sum of all matrix elements
    * The matrix itself
On the first line, you will get matrix sizes in format "{rows}, {columns}"
'''


matrix_type = input().split(', ')

rows = int(matrix_type[0])
columns = int(matrix_type[1])
matrix = []

for r in range(rows):
    row = [int(i) for i in input().split(', ')]
    matrix.append(row)

sum_elements = sum([sum(e) for e in matrix])
print(sum_elements)
print(matrix)
