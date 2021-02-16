
# 01.unique pin codes-----------------------------------------------------------

first_limit = int(input())
second_limit = int(input())
third_limit = int(input())

for i in range(1, first_limit + 1):
    for j in range(1, second_limit + 1):
        for k in range(1, third_limit + 1):

            if i % 2 == 0 and k % 2 == 0:
                if j == 2 or j == 3 or j == 5 or j == 7:
                    print(f'{i} {j} {k}')
