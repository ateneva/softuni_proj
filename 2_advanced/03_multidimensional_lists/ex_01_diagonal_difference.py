
'''
Write a program that finds the difference between the sums of the square
matrix diagonals (absolute value).
    - On the first line, you are given the integer N - the size of the square matrix
    - The next N lines holds the values for every row - N numbers separated by a space
'''

def get_square_matrix(n):
    matrix = []
    for _ in range(n):
        nums = [int(i) for i in input().split()]
        matrix.append(nums)
    return matrix

def calculate_primary(n):
    primary = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                primary_diagonal = square_matrix[i][j]
                primary += primary_diagonal
    return primary

def calculate_secondary(n):
    secondary = 0
    for i in range(n):
        for j in range(n):
            if (i + j) == n-1:
                secondary_diagonal = square_matrix[i][j]
                secondary += secondary_diagonal
    return secondary


n = int(input())
square_matrix = get_square_matrix(n)
primary_d = calculate_primary(n)
secondary_d = calculate_secondary(n)

difference = abs(primary_d - secondary_d)
print(difference)
