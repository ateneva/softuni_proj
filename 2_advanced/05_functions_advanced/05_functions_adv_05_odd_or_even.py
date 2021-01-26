
# ------------------05. odd or even -------------------------------------------

'''
You will receive a command and a list of numbers:
If the command is "Odd":
    Print the sum of the Odd numbers multiplied by the length of the initial list.

If the command is "Even":
    Print the sum of the Even numbers multiplied by the length of the initial list.
'''

def odd_or_even(command, nums):
    numbers = [int(n) for n in nums.split(" ")]
    odd = [o for o in numbers if o % 2 != 0]
    even = [e for e in numbers if e % 2 == 0]

    if command == 'Odd':
        print(sum(odd)*len(numbers))

    elif command == 'Even':
        print(sum(even)*len(numbers))

odd_or_even(input(), input())
