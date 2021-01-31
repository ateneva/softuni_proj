
# --------------------09. Keyword arguments length ----------------------------

'''
Create a function called kwargs_length which can receive different numbers
 of keyword arguments and returns their length.
'''

def kwargs_length(**kwargs):
    result = len([k for k in kwargs])
    return result
