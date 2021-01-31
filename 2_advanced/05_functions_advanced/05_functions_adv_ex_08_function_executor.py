
# -----------------------08 function executor---------------------------------

'''
Create a function called func_executor that can receive different number
    of tuples, each of which will have exactly 2 elements:
    first will be a function
    and the second will be a tuple of the arguments that need to be passed to that function.

    Create a list which will contain all the results of
    the executed functions with its corresponding arguments.
'''

def func_executor(*args):
    result = []
    for a in args:
       function = a[0]
       arguments = a[1]

       # unpack arguments and store in a list
       result.append(function(*arguments))
    return result
