
# half sum element--------------------------------------
import sys

n = int(input())
i_sum = 0
max_count = 0
max_num = -sys.maxsize

for i in range(0, n):
    i = int(input())
    i_sum += i
    max_count += 1

    if i > max_num:
        max_num = i

i_sum -= max_num
if i_sum == max_num:
    print(f'Yes \nSum = {i_sum}')

else:
    diff = abs(max_num - i_sum)
    print(f'No \nDiff = {diff}')
