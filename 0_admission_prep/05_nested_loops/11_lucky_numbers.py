
# 03.lucky numbers -----------------------------------------------------------------

num = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                if (i + j) == (k + l):
                    if num % (i + j) == 0:
                        print(f'{i}{j}{k}{l} ', end='')
