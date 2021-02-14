
# ---------------------problem 3: periodic table-------------------------------

'''
Write a program that keeps all the unique chemical elements.
On the first line you will be given a number n - the count of input lines
that you are going to receive. On the next n lines, you will be receiving
chemical compounds, separated by a single space.

Your task is to print all the unique ones on separate lines
'''

# approach 1: use add set method
n = int(input())

unique_elements = set()
for _ in range(n):
    elements = input().split(" ")
    for element in elements:
        unique_elements.add(element)

for e in unique_elements:
    print(e)

# OR

# approach 2: union a set of the subsequent elements with the original ones
def periodic_table(e):
    n = int(e)
    unique_elements = set()

    for _ in range(n):
        elements = set(input().split(" "))
        unique_elements |= elements                         # union operator
        #unique_elements = unique_elements.union(elements)  # union method

    print('\n'.join(unique_elements))

periodic_table(input())
