
# 12.the song of the wheels--------------------------------------------------------

control = int(input())
is_found = False
count = 0
password = ''

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b:
                    if c > d:
                        if control == (a * b + c * d):
                            print(f'{a}{b}{c}{d} ', end='')
                            count += 1
                            if count == 4:
                                is_found = True
                                password = str(a) + str(b) + str(c) + str(d)
                                break

if is_found:
    print()
    print(f'Password: {password}')
else:
    print()
    print("No!")
