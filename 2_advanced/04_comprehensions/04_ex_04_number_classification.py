
# ------------------------04. number classification---------------------------

'''
Using list comprehension write a program that receives numbers separated by
comma and space ", " and prints all the
 positive, negative, even and odd numbers on separate lines as shown below

Note: Zero is counted for a positive number
'''

def classify_numbes(num_sequence):
    nums = [int(n) for n in num_sequence.split(", ")]

    positives = [str(p) for p in nums if p >= 0]
    negatives = [str(n) for n in nums if n < 0]
    even = [str(e) for e in nums if e % 2 == 0]
    odd = [str(o) for o in nums if o % 2 != 0]

    print(f'Positive: {", ".join(positives)}')
    print(f'Negative: {", ".join(negatives)}')
    print(f'Even: {", ".join(even)}')
    print(f'Odd: {", ".join(odd)}')

classify_numbes(input())
