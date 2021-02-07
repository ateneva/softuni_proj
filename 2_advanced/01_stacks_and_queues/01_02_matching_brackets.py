
# -----------------Problem 2: Matching brackets---------------------------------

'''
We are given an arithmetic expression with brackets.
Scan through the string and extract each sub-expression.
Print the result back on the console
'''

def matching_brackets(text):
    brackets = []

    for i in range(len(text)):
        if text[i] == "(":
            brackets.append(i)

        elif text[i] == ")":
            start_index = brackets.pop()
            print(text[start_index:i + 1])

matching_brackets(input())
