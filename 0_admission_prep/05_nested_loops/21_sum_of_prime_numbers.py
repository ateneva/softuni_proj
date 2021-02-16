
# equal sums (prime/ non-prime) ------------------------------------------------

num = input()
prime = 0
non_prime = 0

while num != 'stop':
    num = int(num)
    if num < 0:
        print(f'Number is negative.')
        num = input()
        continue

    is_not_prime = False

    for i in range(2, num):
        if num % i == 0:
            is_not_prime = True
            break

    if is_not_prime:
        non_prime += num
    else:
        prime += num
    num = input()

print(f'Sum of all prime numbers is: {prime}')
print(f'Sum of all non prime numbers is: {non_prime}')
