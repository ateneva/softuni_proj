
#------------------- Problem 01: even numbers -------------------------------

'''
Write a program that receives a list of numbers. Print only the even numbers from the list.
'''

def even_numbers(num_sequence):
    nums = [int(n) for n in num_sequence.split(" ")]
    evens = [int(n) for n in nums if n % 2 == 0]
    return evens

print(even_numbers(input()))
