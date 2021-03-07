
'''
Write a program that receives text on the first line and times (to repeat the text) that must be an integer.
    If the user passes non-integer type for the times variable, handle the exception
    and print a message  "Variable times must be an integer".

'''

try:
    message = input()
    times = int(input())
    print(message * times)

except ValueError:
    print("Variable times must be an integer")

