
# matrix--------------------------------------------------------------
a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i1 in range(a, b + 1):
    for i2 in range(a, b + 1):
        for j1 in range(c, d + 1):
            for j2 in range(c, d + 1):

                if i1 + j2 == i2 + j1 and i1 != i2 and j1 != j2:
                    print(f'{i1}{i2}')
                    print(f'{j1}{j2}\n')
