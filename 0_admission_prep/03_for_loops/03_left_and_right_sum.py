
# left and right sum--------------------------------------------------
numbers = int(input())
i_count = 0
left_sum = 0
right_sum = 0

for i in range(0, 2*numbers):
    i = int(input())
    i_count += 1

    if i_count <= 2*numbers/2:
        left_sum += i

    elif i_count > 2*numbers/2:
        right_sum += i

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {abs(left_sum-right_sum)}')
