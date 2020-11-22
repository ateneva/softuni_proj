
# ----------------------Problem 2: Maximum and Minimum elements-----------------

# -----100 points ---------
n = int(input())
stack = []

for n in range(n):
    numbers = list(map(lambda x: int(x), input().split(' ')))
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
