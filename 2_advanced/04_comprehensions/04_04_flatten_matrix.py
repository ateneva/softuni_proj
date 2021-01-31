
# -----------------------------04. flatten matrix ------------------------------

'''
Write a program that receives a matrix and prints the flattened version of it.
For example, the flattened list of the matrix: [[1, 2], [3, 4]] will be [1, 2, 3, 4]
'''

def read_matrix():
    rows = int(input())
    matrix = []
    for r in range(rows):
        numbers = [int(n) for n in input().split(", ")]
        matrix.append(numbers)

    return matrix

sublists = read_matrix()
full_matrix = [sublist for sublist in sublists]
flattened_matrix =[s for sublist in sublists for s in sublist]

print(flattened_matrix)
