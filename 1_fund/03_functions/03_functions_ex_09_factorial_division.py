
# ----------------09. factorial division (exam problem)-------------------------

'''
Write a function that receives two integer numbers.
Calculate factorial of each number.
Divide the first result by the second and print the division formatted to the second decimal point.
'''

# --------------100 points --------------------
x = int(input())
y = int(input())

def factorial(x,y):
    for i in range(1, x):
        x *= i

    for j in range(1, y):
        y *= j

    return x/y

print(f'{factorial(x,y):.2f}')
