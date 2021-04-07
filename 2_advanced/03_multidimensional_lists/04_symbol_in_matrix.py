
'''
Write a program that reads N, a number representing the rows and cols of a matrix.
On the next N lines, you will receive rows of the matrix.
Each row consists of ASCII characters. After that, you will receive a symbol.
Find the first occurrence of that symbol in the matrix and print its position
    in the format: "({row}, {col})".
If there is no such symbol print an error message "{symbol} does not occur in the matrix"
'''

N = int(input())

matrix = []
for n in range(N):
    row = input().split()
    matrix.append(row)

symbol = input()
found = False
matrix_position = 0
symbol_position = 0

# print(matrix)

for i in range(len(matrix)):
    for j in matrix[i]:
        if symbol in j:
            symbol_position = j.index(symbol)
            matrix_position += i
            found = True
            break

if found:
    print(f'({matrix_position}, {symbol_position})')
else:
    print(f'{symbol} does not occur in the matrix')