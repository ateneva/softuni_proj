
# 05.challenge the wedding----------------------------------------------------------

men = int(input())
women = int(input())
tables = int(input())
iter = 0
prev = ''

for m in range(1, men + 1):
    for w in range(1, women + 1):
        prev = "(" + str(m) + " <-> " + str(w) + ")"
        iter += 1

        if iter == tables:
            print(f"({m} <-> {w})", end=' ')
            break
        else:
            print(prev, end=' ')
