################################################################################
# ----------------------------Exercises-----------------------------------------

# -----------Problem 1: Reverse numbers with a stack ---------------------------

def reverse(numbers):
    #numbers = input().split(' ')
    stack = []

    for n in range(len(numbers)):
        stack.append(numbers.pop())

    print(' '.join(stack))

reverse(input().split(' '))
