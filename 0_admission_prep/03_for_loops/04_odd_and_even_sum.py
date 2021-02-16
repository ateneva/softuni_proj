
# odd / even sum -------------------------------------------------------
numbers = int(input())
i_count = 0
odd_sum = 0
even_sum = 0

for index in range(0, numbers):
    i = int(input())
    if index % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

if even_sum == odd_sum:
    print(f'Yes\nSum = {even_sum}')
else:
    print(f'No\nDiff = {abs(even_sum-odd_sum)}')
