
# ---------------------------even or odd ---------------------------------------

'''
Create a function called even_odd that can receive different amount of numbers
    and a command at the end.
The command can be "even" or "odd".
Filter the numbers depending on the command and return them in a list.

'''

def even_odd(*args):
    command = args[-1]
    nums = [n for n in args[:-1]]
    if command == 'even':
        numbers = [n for n in nums if n % 2 == 0]
    else:
        numbers = [n for n in nums if n % 2 != 0]

    return numbers
