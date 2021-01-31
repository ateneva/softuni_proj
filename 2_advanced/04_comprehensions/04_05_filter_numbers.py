
# ------------------------05. filter numbers-----------------------------------

'''
You will be given a start and an end.
Print all the numbers in the given range (inclusive)
    that are divisible by any of the numbers from 2 to 10.
'''

# aproach 1: use nested loop
i = int(input())
j = int(input())

divisibles = set()
for n in range(i, j+1):
    for m in range(2, 11):
        if n % m == 0:
            divisibles.add(n)

print(list(divisibles))

# approach 2: use nested comprehension
divs = [n for n in range(i, j+1)
                for m in range(2,11) if n % m ==0
                    ]

print(list(set(divs)))
