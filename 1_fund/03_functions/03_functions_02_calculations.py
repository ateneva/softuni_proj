
# -------------------Problem 02. calculations ----------------------------------

'''
Create a function that receives three parameters and calculates a result depending on operator.
The operator can be 'multiply', 'divide', 'add', 'subtract' .
The input comes as three parameters – two integers and an operator as a string.
'''

# --------------100 points --------------------
operator = input()
param1 = int(input())
param2 = int(input())

def calc(operator, param1, param2):

    if operator == 'multiply':
        return param1 * param2

    elif operator == 'divide':
        return param1/param2

    elif operator == 'add':
        return param1 + param2

    elif operator == 'subtract':
        return param1 - param2

# needs to printed with all parameters, else throws an error
print(int(calc(operator, param1, param2)))
