
# -----------------Problem 3: Record Unique Names ----------------------------

'''
Write a program, which will take a list of names and print only the unique names in the list.
The order in which we print the result does not matter.
'''

num_names = int(input())
unique_names = []

for name in range(1, num_names + 1):
    name = input()

    if name not in unique_names:
        unique_names.append(name)

for n in unique_names:
    print(n)


# OR

n = int(input())
unique_names = set()

for i in range(n):
    unique_names.add(input())

for person in unique_names:
    print(person)