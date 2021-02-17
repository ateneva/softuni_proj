
# ---------------problem 7: flatten strings--------------------------------------

'''
Write a program to flatten several lists of numbers, received in the following format:
 - String with numbers separated by '|'.
 - Values are separated by spaces (' ', one or several)
 - Order the output list from the last to the first received, and their values from left to right

'''

string = input()

flattened = [" ".join(f.split()) for f in string.split("|")]
reversed_order = [f for f in flattened[::-1] if f != '']

print(' '.join(reversed_order))