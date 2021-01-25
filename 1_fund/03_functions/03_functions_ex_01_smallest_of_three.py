

# --------------------01. smallest of three numbers ----------------------------

'''
Write a function which receives three integer numbers and returns the smallest.
Use appropriate name for the function.
'''

# --------------100 points --------------------
a = int(input())
b = int(input())
c = int(input())

def smallest_of_three(a, b, c):
    return min(a, b, c)

print(smallest_of_three(a, b, c))
