
# special numbers---------------------------------------------------------------

num = int(input())

for i in range(1111, 10000):
    i = str(i) # need to convert to string to extract the individual elements

    d1 = int(i[0])
    d2 = int(i[1])
    d3 = int(i[2])
    d4 = int(i[3])

    if d1 > 0 and num % d1 == 0:
        if d2 > 0 and num % d2 == 0:
            if d3 > 0 and num % d3 == 0:
                if d4 > 0 and num % d4 == 0:
                    print(f'{i} ', end='')
