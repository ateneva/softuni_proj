
# -----------------03. multiplication function----------------------------------

'''
Write a function called multiply that can receive any number
of  different parameters and returns the result of the multiplication of all of them.
'''

def multiply(*args):
    result = 1
    for x in args:
        result *= x
    return result
