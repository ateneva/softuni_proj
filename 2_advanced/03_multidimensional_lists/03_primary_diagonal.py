
'''
Write a program that finds the sum of matrix primary diagonal
'''

N = int(input())

matrix = []
for n in range(N):
    row = [int(i) for i in input().split(' ')]
    matrix.append(row)

# print(matrix)
# diagonal = matrix[0][0] + matrix[1][1] + matrix[2][2]
# print(diagonal)

diagonal_sum = 0

for i in range(len(matrix)):
    diagonal_sum += matrix[i][i]

print(diagonal_sum)
