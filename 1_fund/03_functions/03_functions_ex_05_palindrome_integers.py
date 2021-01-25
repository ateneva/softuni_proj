
# ------------------------05. palindrome integers ------------------------------

'''
A palindrome is a number which reads the same backward as forward, such as 323 or 1001.
Write a function which receives a list of positive integers
    and checks if each integer is a palindrome or not.
Print the results on the console

The input will be a single string containing the numbers separated by comma and space ", "
'''

# --------------100 points --------------------
numbers = input()

def palindrome(numbers):
    result = []
    numbers = numbers.split(',')
    for num in numbers:
        num = num.lstrip()
        #print(''.join(list(num)))
        #print(''.join(list(reversed(num))))
        if ''.join(list(num)) == ''.join(list(reversed(num))):
            result.append('True')
        else:
            result.append('False')
    return result

for r in palindrome(numbers):
    print(r)
