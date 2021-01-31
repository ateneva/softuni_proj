
# -----------------------02. sort -----------------------------------------

'''
Write a program that prints a sorted list of numbers in ascending order.
'''

def sort_values(value_sequence):
    values = [int(v) for v in value_sequence.split(" ")]
    values.sort()
    return values

print(sort_values(input()))
