
# 04.car number --------------------------------------------------------------------

num1 = int(input())
num2 = int(input())

for i in range(num1, num2 + 1):
    for j in range(num1, num2 + 1):
        for k in range(num1, num2 + 1):
            for l in range(num1, num2 + 1):
                if (i % 2 == 0 and l % 2 != 0) \
                     or  (i % 2 != 0 and l % 2 == 0):
                        if i > l:
                            if (j + k) % 2 == 0:
                                print(f'{i}{j}{k}{l} ', end='')
