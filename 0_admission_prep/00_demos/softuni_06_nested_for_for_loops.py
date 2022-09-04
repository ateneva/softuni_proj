
# multiplication table---------------------------------------------------------
for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} * {j} = {i * j}')


# clock ------------------------------------------------------------------------
for h in range(24):
    for m in range(60):
        for s in range(60):
            print(f'{h} : {m} : {s}')

# combinations-----------------------------------------------------------------
n = int(input())
combinations = 0

for x1 in range(0, n + 1):
    for x2 in range(0, n + 1):
        for x3 in range(0, n + 1):
            if x1 + x2 + x3 == n:
                combinations += 1

print(combinations)

# matrix------------------------------------------------------------------------
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


# building----------------------------------------------------------------------

floors = int(input())
spaces = int(input())

for i in range(floors, 0, -1):  # looping in reverse order
    for j in range(spaces):

        if floors == 1 \
                or (i % 2 == 0 and i == floors) \
                or (i % 2 != 0 and i == floors):
            print('L{0}{1} '.format(i, j), end="")  # large apartments

        elif i % 2 == 0 and i != floors:  # office
            print('O{0}{1} '.format(i, j), end="")

        elif i % 2 != 0 and i != floors:  # apartments
            print('A{0}{1} '.format(i, j), end="")

    print()  # starting on a new line


# sum of two numbers------------------------------------------------------------

start = int(input())
end = int(input())
magic_num = int(input())
combination = 0
combinations = 0
isFound = False

for i in range(start, end + 1):
    for j in range(start, end + 1):
        combinations += 1
        if i + j == magic_num:
            isFound = True
            print(f'Combination N:{combinations} ({i} + {j} = {magic_num})')
            break
    if isFound:
        break

if isFound == False:
    print(f'{combinations} combinations - neither equals {magic_num}')


 # 01.unique pin codes----------------------------------------------------------

first_limit = int(input())
second_limit = int(input())
third_limit = int(input())

for i in range(1, first_limit + 1):
    for j in range(1, second_limit + 1):
        for k in range(1, third_limit + 1):

            if i % 2 == 0 and k % 2 == 0:
                if j == 2 or j == 3 or j == 5 or j == 7:
                    print(f'{i} {j} {k}')

# 02.letter combinations--------------------------------------------------------

first = input()
second = input()
third = input()
count = 0

for i in range(ord(first), ord(second)+1):
    for j in range(ord(first), ord(second)+1):
        for k in range(ord(first), ord(second)+1):
            if chr(i) != third and chr(j) != third and chr(k) != third:
                count += 1
                print(f'{chr(i)}{chr(j)}{chr(k)} ', end='')
print(count)

# 03.lucky numbers -------------------------------------------------------------

num = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                if (i + j) == (k + l):
                    if num % (i + j) == 0:
                        print(f'{i}{j}{k}{l} ', end='')

# 04.car number ----------------------------------------------------------------

num1 = int(input())
num2 = int(input())

for i in range(num1, num2 + 1):
    for j in range(num1, num2 + 1):
        for k in range(num1, num2 + 1):
            for l in range(num1, num2 + 1):
                if (i % 2 == 0 and l % 2 != 0) \
                     or  (i % 2 != 0 and l % 2 == 0):
                        if i > l:
                            if (j + k) % 2 == 0:
                                print(f'{i}{j}{k}{l} ', end='')


# 06.wedding seats--------------------------------------------------------------

aisle = input()
rows = int(input())
seats = int(input())
count_seats = 0

for a in range(65, ord(aisle) + 1):
    if a > 65:
        rows += 1   # rows increase by 1 in every sector after A

    for r in range(1, rows + 1):
        if r % 2 != 0:                # seats in even rows are by 2 more
            for s in range(97, 97 + seats):
                print(f'{chr(a)}{r}{chr(s)}')
                count_seats += 1
        else:
            even_seats = seats + 2
            for s in range(97, 97 + even_seats):
                print(f'{chr(a)}{r}{chr(s)}')
                count_seats += 1

print(count_seats)

# 07.safe passwords generator---------------------------------------------------

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

# 09.sum of two numbers---------------------------------------------------------

start = int(input())
end = int(input())
magic_number = int(input())
comb = 0
is_found = False

for i in range(start, end + 1):
    for j in range(start, end + 1):
        comb += 1
        magic = comb
        if ((i + j) or (j + i) )== magic_number:
            is_found = True
            break

    if is_found:
        print(f"Combination N:{comb} ({i} + {j} = {magic_number})")
        break

if not is_found:
    print(f"{comb} combinations - neither equals {magic_number}")


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



 # *************Mock Exam 2019-10-27 multiplication table **********************
number = int(input())

start = int(str(number)[-1:])
mid = int(str(number)[-2])
end = int(str(number)[:1])

for i in range(1, start+1):
    for j in range(1, mid+1):
        for k in range(1, end+1):
            print(f'{i} * {j} * {k} = {i * j * k};')

 # **********06.movie tickets (nested loop) ************************************

a1 = int(input())
a2 = int(input())
n = int(input())
ticket = ''

for i in range(a1, a2):
    for j in range(1, n):
        for k in range(1, n//2):
            ticket = chr(i) + '-' + str(j) + str(k) + str(i)

            if i % 2 != 0 \
                 and (i + j + k) % 2 != 0:
                 print(ticket)

# **********nested loops exercises (fishing) ***********************************

quota = int(input())
fish_caught = 0
balance = 0
stop = False

for fish in range(quota):
    fish_name = input()
    if fish_name == 'Stop':
        stop = True
        break

    fish_weight = float(input())
    fish_caught += 1

    fish_value = 0
    for value in fish_name:
        money = ord(value)
        fish_value += money

    fish_value /= fish_weight

    if fish_caught % 3 == 0:
        balance += fish_value
    else:
        balance -= fish_value

if not stop:
    print(f'Lyubo fulfilled the quota!')

if balance >= 0:
    print(f"Lyubo's profit from {fish_caught} fishes is {balance:.2f} leva.")
else:
    print(f"Lyubo lost {abs(balance):.2f} leva today.")

# ************06. 2019-11-03 Admission Exam gold mine (nested mine)*************

locations = int(input())
total_retrieved = 0
avg_retrieved = 0
days_mined = 0
stop = False

for location in range(1, locations + 1):
    expected = float(input())
    days = int(input())

    for day in range(1, days + 1):
        retrieved = float(input())
        total_retrieved += retrieved

        avg_retrieved = total_retrieved/days

    if avg_retrieved >= expected:
        print(f"Good job! Average gold per day: {avg_retrieved:.2f}.")
    else:
        print(f"You need {abs(avg_retrieved - expected):.2f} gold.")

    total_retrieved = 0
    avg_retrieved = total_retrieved / days

# 11.happy cat parking----------------------------------------------------------

days = int(input())
hours = int(input())
fee = 0
total_fees = 0

for d in range(1, days + 1):
    day_total = 0

    for h in range(1, hours + 1):
        if d % 2 == 0 and h % 2 != 0:
            fee = 2.50
        elif d % 2 != 0 and h % 2 == 0:
            fee = 1.25
        else:
            fee = 1.00

        day_total += fee

    print(f"Day: {d} - {day_total:.2f} leva")

    total_fees += day_total

print(f"Total: {total_fees:.2f} leva")


# 12.the song of the wheels-----------------------------------------------------

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



# **********06.vet parking (nested loop) ***************************************

days = int(input())
hours = int(input())
fee = 0
total_fees = 0

for d in range(1, days + 1):
    day_total = 0

    for h in range(1, hours + 1):
        if d % 2 == 0 and h % 2 != 0:
            fee = 2.50
        elif d % 2 != 0 and h % 2 == 0:
            fee = 1.25
        else:
            fee = 1.00

        day_total += fee

    print(f"Day: {d} - {day_total:.2f} leva")

    total_fees += day_total

print(f"Total: {total_fees:.2f} leva")
