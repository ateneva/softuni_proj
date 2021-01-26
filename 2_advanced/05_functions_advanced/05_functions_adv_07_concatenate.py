
# ----------------------05. concatenate ----------------------------------------

'''
Write a function called concatenate() that receives some strings,
    concatenates them and returns the result
'''

def concatenate(*args):
    concatenation = ''
    for s in args:
        concatenation += s
    return concatenation

print(concatenate("Soft", "Uni", "Is", "Great", "!"))
