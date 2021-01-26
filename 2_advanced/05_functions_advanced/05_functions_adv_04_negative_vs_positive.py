
# ----------------------04. negative vs. postive--------------------------------

'''
You will receive a list of numbers. Separate the negative numbers from the positive.
Find the total sum of the negatives and positives, replace the negative number
    with its absolute value and print the following:
        
    If the absolute negative number is bigger than the positive number:
    	"The negatives are stronger than the positives"
    If the positive number is bigger than the absolute negative number:
    	"The positives are stronger than the negatives"

'''

def negative_or_postive(nums):
    numbers = [int(n) for n in nums.split(" ")]
    negatives = [n for n in numbers if n < 0]
    positives = [p for p in numbers if p > 0]
    total_negatives = abs(sum(negatives))
    total_positives = sum(positives)
    print(total_negatives*-1)
    print(total_positives)

    if total_negatives > total_positives:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")

negative_or_postive(input())
