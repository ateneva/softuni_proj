
'''
Write a function called list_manipulator which receives a list of numbers as first parameter and different amount of other parameters. The second parameter might be "add" or "remove". The third parameter might be "beginning" or "end". There might or might not be any other parameters (numbers):
 - In case of "add" and "beginning",
    add the given numbers to the beginning of the given list of numbers
    and return the new list

 - In case of "add" and "end",
    add the given numbers to the end of the given list of numbers
    and return the new list

 - In case of "remove" and "beginning"
    - If there is another parameter (number), remove that amount of numbers from
        the beginning of the list of numbers.
    - If there are no other parameters, remove only the first element of the list.
    - Finaly, return the new list

 - In case of "remove" and "end"
    - If there is another parameter (number), remove that amount of numbers from
    the end of the list of numbers.
    - Otherwise if there are no other parameters, remove only the last element of the list.
    - Finaly, return the new list
'''

from collections import deque

def list_manipulator(nums, *args):
    numbers = deque(nums)
    parameters = len(args)
    action = args[0]
    direction = args[1]

    if action == 'add' and direction == 'beginning':
        if parameters > 2:
            items = []
            for a in args[2:]:       # get all extra numbers
                items.append(a)

            for i in items[::-1]:    # add them to front starting from the last one
                numbers.appendleft(i)
        return list(numbers)

    elif action == 'add' and direction == 'end':
        if parameters > 2:
            items = []
            for a in args[2:]:      # get all extra numbers
                items.append(a)

            for i in items:
                numbers.append(i)   # add them to original list one by one
        return list(numbers)

    elif action == 'remove' and direction == 'beginning':
        if parameters > 2:
            items = args[2]
            for _ in range(items):
                numbers.popleft()
        else:
            numbers.popleft()
        return list(numbers)

    elif action == 'remove' and direction == 'end':
        if parameters > 2:
            items = args[2]
            for _ in range(items):
                numbers.pop()
        else:
            numbers.pop()
        return list(numbers)

print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))

print(list_manipulator([1,2,3], "add", "beginning", 20))

print(list_manipulator([1,2,3], "add", "end", 30))

print(list_manipulator([1,2,3], "remove", "end", 2))

print(list_manipulator([1,2,3], "remove", "beginning", 2))

print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
