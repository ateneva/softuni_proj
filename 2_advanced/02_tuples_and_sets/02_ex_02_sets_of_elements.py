
# ------------------problem 2: sets of elements--------------------------------

'''
Write a program that prints a set of elements.
On the first line, you will receive two numbers - n and m,
which represent the lengths of two separate sets.

On the next n + m lines you will receive n numbers, which are the numbers in the
first set, and m numbers, which are in the second set.

Find all the unique elements that appear in both
    and print them on separate lines (the order does not matter).
'''

# approach 1: usng sets and loops
nums = input().split(" ")

set_one = int(nums[0])
set_two = int(nums[1])

a = set()
b = set()
for n in range(set_one):
    element = int(input())
    a.add(element)

for m in range(set_two):
    elem = int(input())
    b.add(elem)

unique_set_numbers = set(a & b)
for n in unique_set_numbers:
    print(n)

# OR

# approach 2: using set comprehensions
def sets_of_elements(numbers):
    nums = numbers.split(" ")
    set_one = int(nums[0])
    set_two = int(nums[1])

    a = {int(input()) for n in range(set_one)}
    b = {int(input()) for m in range(set_two)}

    unique_set_numbers = set(a & b)
    [print(n) for n in unique_set_numbers]

sets_of_elements(input())
