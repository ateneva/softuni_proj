
# -------------------------02. add and subtract --------------------------------

'''
You will receive three integer numbers.
Write a function sum_numbers() to get the sum of the first two integers
    and subtract() function that subtracts the third integer from the result.

Wrap the two functions in a function called add_and_subtract(),
    which will receive the three numbers
'''

# --------------100 points --------------------
a = int(input())
b = int(input())
c = int(input())

def sum_numbers(a, b):
    return a + b

def subtract(sum_numbers, c):
    return sum_numbers - c

def add_and_subtract(a, b, c):
    sum_numbers(a,b)
    subtract(sum_numbers(a,b,),c)

print(subtract(sum_numbers(a,b,),c))
