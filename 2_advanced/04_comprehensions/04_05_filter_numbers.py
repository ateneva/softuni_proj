
# ------------------------05. filter numbers-----------------------------------

'''
You will be given a start and an end.
Print all the numbers in the given range (inclusive)
    that are divisible by any of the numbers from 2 to 10.
'''

# aproach 1: use nested loop
def filter_numbers(i, j):
    divisibles = set()
    for n in range(i, j+1):
        for m in range(2, 11):
            if n % m == 0:
                divisibles.add(n)

    print(list(divisibles))
filter_numbers(int(input()), int(input()))


# approach 2: use nested comprehension
def filter_numbers_app_two(i, j):
    divs = [n for n in range(i, j+1)
                    for m in range(2,11) if n % m ==0
                        ]
    print(list(set(divs)))

filter_numbers_app_two(int(input()), int(input()))
