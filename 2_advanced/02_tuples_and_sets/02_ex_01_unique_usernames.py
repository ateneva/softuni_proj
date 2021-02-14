
# ----------------problem 1: unique names-------------------

'''
Write a program that reads from the console a sequence of N usernames and
keeps a collection only of the unique ones.
On the first line, you will receive an integer N.
On the next N lines, you will receive a username.
Print the collection on the console (the order does not matter):

'''

def get_unique_names(names_count):
    num = int(names_count)

    unique_names = set()
    for n in range(num):
        name = input()
        unique_names.add(name)

    for name in unique_names:
        print(name)

get_unique_names(input())
