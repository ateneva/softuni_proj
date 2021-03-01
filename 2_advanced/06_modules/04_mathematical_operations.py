
'''
You will receive a single string in the following format
"{number1} {sign} {number2}"
 - number1 - a float number in the range (0.0, 1000.0)
 - sign - a char that can be
        '/' - divide the first number with the second
        '*' - multiply the 2 numbers
        '-' - subtract the first number with the second
        '+' - add the 2 numbers
        '^' - raise the first number to the second
 - number2 - an integer number in the range (0, 1000)

'''

def mathematical_operations(inputs):
    num_one = float(inputs[0])
    operator = inputs[1]
    num_two = int(inputs[2])

    if operator == '/':
        result = num_one / num_two

    elif operator == '*':
        result = num_one * num_two

    elif operator == '-':
        result = num_one - num_two

    elif operator == '+':
        result = num_one + num_two

    elif operator == '^':
        result = num_one ** num_two

    print(f'{result:.2f}')
    return result

mathematical_operations(input().split())
