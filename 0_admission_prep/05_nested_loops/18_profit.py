

# 10.profit---------------------------------------------------------------------

ones = int(input())
twos = int(input())
fives = int(input())
total = int(input())

for o in range(0, ones + 1):
    for t in range(0, twos + 1):
        for f in range(0, fives + 1):
            if (o*1 + t*2 + f*5) == total:
                print(f"{o} * 1 lv. + {t} * 2 lv. + {f} * 5 lv. = {total} lv.")
