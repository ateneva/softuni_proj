
# clock-----------------------------------------------------------------------
for h in range(24):
    for m in range(60):
        print(f'{h}:{m}')

# clock part 2----------------------------------------------------------------
for h in range(24):
    for m in range(60):
        for s in range(60):
            print(f'{h} : {m} : {s}')

# multiplication table---------------------------------------------------------
for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} * {j} = {i * j}')

# combinations-----------------------------------------------------------------
n = int(input())
combinations = 0

for x1 in range(0, n + 1):
    for x2 in range(0, n + 1):
        for x3 in range(0, n + 1):
            if x1 + x2 + x3 == n:
                combinations += 1

print(combinations)
