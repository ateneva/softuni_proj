
# odd/even position------------------------------------------------------------
import sys

n = int(input())
odd_sum = 0
odd_max = -sys.maxsize
odd_min = sys.maxsize

even_sum = 0
even_max = -sys.maxsize
even_min = sys.maxsize

for index in range(1, n+1):
    i = float(input())

    if index % 2 == 0:
        even_sum += i

        if i > even_max:
            even_max = i

        if i < even_min:
            even_min = i

    else:
        odd_sum += i

        if i > odd_max:
            odd_max = i

        if i < odd_min:
            odd_min = i

print(f'OddSum=%.2f,' % odd_sum)

if odd_min == sys.maxsize:
    print('OddMin=No,')
else:
    print(f'OddMin=%.2f,' % odd_min)

if odd_max == -sys.maxsize:
    print('OddMax=No,')
else:
    print(f'OddMax=%.2f,' % odd_max)

print(f'EvenSum=%.2f,' % even_sum)

if even_min == sys.maxsize:
    print('EvenMin=No,')
else:
    print(f'EvenMin=%.2f,' % even_min)

if even_max == -sys.maxsize:
    print('EvenMax=No')
else:
    print(f'EvenMax=%.2f' % even_max)
