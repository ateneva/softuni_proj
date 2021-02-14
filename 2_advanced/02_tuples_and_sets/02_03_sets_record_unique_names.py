
# -----------------Problem 3: Record Unique Names ----------------------------

'''
Write a program, which will take a list of names and print only the unique names in the list.
The order in which we print the result does not matter.
'''
# approach 1: using list
num_names = int(input())
unique_names = []

for name in range(1, num_names + 1):
    name = input()

    if name not in unique_names:
        unique_names.append(name)

for n in unique_names:
    print(n)

# OR
# approach 2: using set
n = int(input())
unique_names = set()

for i in range(n):
    unique_names.add(input())

for person in unique_names:
    print(person)

# OR
# approach 3: using a list comprehension and set
n = int(input())
unique_names = set()
[unique_names.add(input()) for i in range(n)]
[print(person) for person in unique_names]

# OR
# approach 4: using a set comprehension
n = int(input())
unique_names = {(input()) for i in range(n)}
[print(person) for person in unique_names]
