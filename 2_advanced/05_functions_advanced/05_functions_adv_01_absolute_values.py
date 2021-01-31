
# -------------------------01. absolute values --------------------------------

'''
Write a program that receives a list of numbers and prints their absolute value.
'''

def absolute_values(nums):
    numbers = nums.split(' ')
    absolute = [abs(float(n)) for n in numbers]
    return absolute

print(absolute_values(input()))
