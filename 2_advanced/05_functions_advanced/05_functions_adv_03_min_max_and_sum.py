
# -----------------------03. min, max and sum======----------------------------

'''
Write a program that prints the min and max values from a list
    and the sum of all the numbers in the list. 
'''

def stats(value_sequence):
    values = [int(v) for v in value_sequence.split(" ")]
    min_value = min(values)
    max_value = max(values)
    sums = sum(values)
    print(f'The minimum number is {min_value}')
    print(f'The maximum number is {max_value}')
    print(f'The sum number is: {sums}')


stats(input())
