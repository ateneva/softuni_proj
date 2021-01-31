
# ---------------------04. even matrix ----------------------------------------

'''
Write a program that receives a matrix of numbers
    and prints a new one only with the numbers that are even.
'''

def read_matrix():
    rows = int(input())
    matrix = []
    for r in range(rows):
        numbers = [int(n) for n in input().split(", ")]
        matrix.append(numbers)

    return matrix

def filter_matrix(evens):
    return [e for e in evens if e % 2 == 0]

nested_lists = read_matrix()
print([filter_matrix(f) for f in nested_lists])
