
# 08.secret door's lock---------------------------------------------------------

hundreds = int(input())
tens = int(input())
ones = int(input())

for h in range(1, hundreds + 1):
    for t in range(1, tens + 1):
        for o in range(1, ones + 1):
            if h % 2 == 0 and o % 2 == 0:
                if t == 2 or t == 3 or t == 5 or t == 7:
                    print(f'{h} {t} {o}')
