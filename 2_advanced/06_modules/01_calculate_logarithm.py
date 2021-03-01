
from math import log

def calculate_logarithm(number, base):
    if base == 'natural':
        logarithm = log(number)
    else:
        logarithm = log(number, int(base))

    print(f'{logarithm:.2f}')
    return logarithm

calculate_logarithm(int(input()), input())


