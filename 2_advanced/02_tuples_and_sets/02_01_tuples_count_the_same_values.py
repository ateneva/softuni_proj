
#--------------------- Problem 1: count the same values------------------------

'''
You will be given a list of numbers.
Write a program that prints the number of occurrences of each number.
'''

def count_the_same_values(nums):
    sequence = tuple([float(s) for s in nums.split(" ")])
    occurences = {}

    for s in sequence:
        if s not in occurences:
            occurences[s] = 0
        occurences[s] += 1

    for k, v in occurences.items():
        print(f'{k} - {v} times')

count_the_same_values(input())
