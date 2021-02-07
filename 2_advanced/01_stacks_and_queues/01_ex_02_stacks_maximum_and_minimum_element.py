
# ----------------------Problem 2: Maximum and Minimum elements-----------------

'''
You have an empty sequence, and you will be given N queries.
Each query is one of these three types:
1 – Push the element x into the stack.
2 – Delete the element present at the top of the stack.
3 – Print the maximum element in the stack.
4 – Print the minimum element in the stack.
After you go through all the queries, print the stack in the following format:
"{n}, {n1}, {n2} …, {nn}"

'''

# -----100 points ---------

n = int(input())
stack = []

for n in range(n):
    numbers = [int(x) for x in input().split(' ')]
    activity = numbers[0]

    if activity == 1:
        stack.append(numbers[1])

    elif activity == 2:
        if stack:       # check if stack has any elements in it
            stack.pop()

    elif activity == 3:
        if stack:
            print(max(stack))

    elif activity == 4:
        if stack:
            print(min(stack))

print_format = [str(x) for x in stack][::-1]
print(', '.join(print_format))
