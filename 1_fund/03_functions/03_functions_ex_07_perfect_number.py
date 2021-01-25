
# -------------------------07. perfect number ----------------------------------

'''
Write a function that receives an integer number and returns if this number is perfect or NOT.
A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
That is the sum of its positive divisors excluding the number itself (also known as its aliquot sum).
'''

# --------------100 points --------------------
numb = int(input())

def is_perfect(numb):
    divisors = []
    for i in range(1, numb):
        if numb % i == 0:
            divisors.append(i)
    return sum(divisors) == numb

if is_perfect(numb):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
