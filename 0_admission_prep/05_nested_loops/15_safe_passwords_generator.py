
# 07.safe passwords generator------------------------------------------------------

a = int(input())
b = int(input())
max_passwords = int(input())
comb = 0
passwords = a * b
prev = ''

for A in range(35, 56):
    for B in range(64, 97):
        for x in range(1, a + 1):
            firstx = x
            x += 1
            for y in range(1, b + 1):
                comb += 1
                firstA = A
                firstB = B
                firsty = y
                A += 1
                B += 1
                y += 1

                if firsty <= b:
                    password = chr(firstA) + chr(firstB) + str(firstx) + str(firsty) + chr(firstB) + chr(firstA) + "|"
                else:
                    password = chr(A) + chr(B) + str(x) + str(y) + chr(B) + chr(A) + "|"

                prev += password

                if passwords <= max_passwords:
                    if passwords == comb:
                        print(prev, end='')

                elif passwords > max_passwords:
                     if max_passwords == comb:
                        print(prev, end='')
    break
