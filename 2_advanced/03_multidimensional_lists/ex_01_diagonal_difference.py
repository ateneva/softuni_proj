
'''
Write a program that finds the difference between the sums of the square
matrix diagonals (absolute value).
    - On the first line, you are given the integer N - the size of the square matrix
    - The next N lines holds the values for every row - N numbers separated by a space
'''

size = int(input())
matrix = []
primary = 0
secondary = 0

for _ in range(size):
    nums = [int(i) for i in input().split()]
    matrix.append(nums)

#print(matrix)

for i in range(size):
    for j in range(size):
        if i == j:
            primary_diagonal = matrix[i][j]
            primary += primary_diagonal

# print(primary)

for i in range(size):
    for j in range(size):
        if (i + j) == size-1:
            secondary_diagonal = matrix[i][j]
            secondary += secondary_diagonal

# print(secondary)

difference = abs(primary - secondary)
print(difference)
