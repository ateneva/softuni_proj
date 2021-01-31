
# -----------------------02. rounded numbers ----------------------------------

'''
Write a program that rounds all the given numbers.
'''

def rounded_values(nums):
    numbers = nums.split(' ')
    rounded = [round(float(n)) for n in numbers]
    return rounded

print(rounded_values(input()))
