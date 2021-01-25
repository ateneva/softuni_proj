
# -----------------------03. repeat string -------------------------------------

'''
Write a function that receives a string and a repeat count n.
The function should return a new string (the old one repeated n times).
'''

# --------------100 points --------------------
string = input()
repeat = int(input())

def rep(string, repeat):
    return string * repeat

# needs to printed with all parameters, else throws an error
print(rep(string, repeat))
