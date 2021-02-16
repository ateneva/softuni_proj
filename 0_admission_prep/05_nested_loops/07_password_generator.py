

# password generator -----------------------------------------------------------

n = int(input())
l = int(input())
letter = 97 + l

for i in range(1, n+ 1):
    for j in range(1, n + 1):
        for k in range(97, letter):
            for l in range(97, letter):
                for m in range(1, n + 1):
                    if m > i and m > j:
                        print(f'{i}{j}{chr(k)}{chr(l)}{m} ', end='')
