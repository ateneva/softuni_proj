
#------------------------Problem 1: Reverse Strings----------------------------

'''
Write program that:
•	Reads an input string
•	Reverses it using a stack
•	Prints the result back on the console
'''

def reverse_strings_stack(text):
    stack = []
    reversed_text = []

    for ch in text:         # convert string to list
        stack.append(ch)

    while stack:
        ch = stack.pop()
        reversed_text.append(ch)

    print(''.join(reversed_text))

# -----approach 2--------------
def reverse_string(text):
    return text[::-1]
    print(reverse_string(text))

# -----approach 3-------------
def reverse_string_list(text):
    text_string = list(text)
    stack = []

    for i in range(len(text_string)):
        stack.append(text_string.pop())

    print("".join(stack))


if __name__ == '__main__':
    reverse_strings_stack(input())
    reverse_string(input())
    reverse_string_list(input())
