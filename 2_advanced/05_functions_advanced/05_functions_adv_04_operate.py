
# --------------------------04. operate ---------------------------------------

'''
Write a function called operate that receives an operator(+, -, * or /)
as first argument and multiple numbers as additional arguments (*args).
The function should return the result of the operator applied to all the numbers.
'''

def operate(operator, *numbers):
    def get_initial_value(operator):
        if operator in ('+', '-'):
            return 0
        else:
            return 1

    result = get_initial_value(operator)

    for x in numbers:
        if operator == '+':
            result += x
        elif operator == '-':
            result -= x
        elif operator == '*':
            result *= x
        else:
            result /= x
    return result
