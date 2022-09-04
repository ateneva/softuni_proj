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


# Mock Exam 2019-10-27 multiplication table ************************************
number = int(input())

start = int(str(number)[-1:])
mid = int(str(number)[-2])
end = int(str(number)[:1])

for i in range(1, start+1):
    for j in range(1, mid+1):
        for k in range(1, end+1):
            print(f'{i} * {j} * {k} = {i * j * k};')

# combinations-----------------------------------------------------------------
n = int(input())
combinations = 0

for x1 in range(0, n + 1):
    for x2 in range(0, n + 1):
        for x3 in range(0, n + 1):
            if x1 + x2 + x3 == n:
                combinations += 1

print(combinations)

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

# travelling--------------------------------------------------------------------
destination = input()

while destination != 'End':
    budget = float(input())
    savings = 0
    has_given_up = False

    while savings < budget:
        current_input = input()
        if current_input == 'End':
            has_given_up = True
            break
        current_savings = float(current_input)
        savings += current_savings

    if has_given_up:
        break

    print(f'Going to {destination}!')
    destination = input()

# name wars---------------------------------------------------------------------
winner = None
winner_sum = 0
sum = 0

while True:
    name = input()

    if name == 'STOP':
        break

    for char in name:
        sum += ord(char)

    if sum >= winner_sum:
        winner_sum = sum
        winner = name

    sum = 0

print(f'Winner is {winner} - {winner_sum}!')

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

# cookie factory----------------------------------------------------------------
doses = int(input())

for batch in range(1, doses + 1):
    flour = False
    sugar = False
    eggs = False
    has_all_ingredients = False
    ingredient = ''

    while True:
        ingredient = input()

        if ingredient == 'flour':
            flour = True

        elif ingredient == 'sugar':
            sugar = True

        elif ingredient == 'eggs':
            eggs = True

        has_all_ingredients = flour and sugar and eggs
        if ingredient == 'Bake!':
            if not has_all_ingredients:
                print('The batter should contain flour, eggs and sugar!')
            else:
                print(f'Baking batch number {batch}...')
                break

# cinema tickets (exam problem)-------------------------------------------------
movie = input()
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while movie != 'Finish':
    seats = int(input())
    seats_taken = 0
    while seats_taken < seats:
        ticket = input()

        if ticket == 'End':
            break
        seats_taken += 1

        if ticket == 'student':
            student_tickets += 1

        elif ticket == 'standard':
            standard_tickets += 1

        elif ticket == 'kid':
            kid_tickets += 1

    capacity = seats_taken / seats * 100
    print(f'{movie} - {capacity :.2f}% full.')
    movie = input()

tickets = student_tickets + standard_tickets + kid_tickets
print(f'Total tickets: {tickets}')
print(f'{student_tickets / tickets * 100 :.2f}% student tickets.')
print(f'{standard_tickets / tickets * 100 :.2f}% standard tickets.')
print(f'{kid_tickets / tickets * 100 :.2f}% kids tickets.')

# -------------------------------------------Exercies---------------------------
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

# number pyramid----------------------------------------------------------
n = int(input())
current = 1
is_current_bigger_than_n = False

for row in range(1, n+1):
    for col in range(1, row+1):
        if current > n:
             is_current_bigger_than_n = True
             break
        print(str(current) + ' ', end='')
        current += 1
    if is_current_bigger_than_n:
        break
    print()

# coding-------------------------------------------------------------------
digit = input()

for digit in reversed(digit):
    num = int(digit)
    for i in range(num):
        if num != 0:
            symbol = chr(num + 33)
            print(symbol, end='')
    if num == 0:
        print('ZERO')
    else:
        print()

# equal sums (even/odd positions) ----------------------------------------------

a = int(input())
b = int(input())

for num in range(a, b+1):
    num = str(num)

    first = int(num[0])
    second = int(num[1])
    third = int(num[2])
    fourth = int(num[3])
    fifth = int(num[4])
    sixth = int(num[5])

    odd_position = fifth + third + first
    even_position = sixth + fourth + second

    are_equal = odd_position == even_position

    if are_equal:
        print(num, end=' ')


# equal sums (even/odd positions - 2nd approach) -------------------------------
a = int(input())
b = int(input())

for num in range(a, b+1):
    num = str(num)
    odd_position = 0
    even_position = 0

    for index in range(len(num)):
        if index % 2 == 0:
            even_position += int(num[index])
        else:
            odd_position += int(num[index])

    are_equal = odd_position == even_position

    if are_equal:
        print(num, end=' ')


# equal sums (left/right positions) --------------------------------------------

a = int(input())
b = int(input())

for num in range(a, b+1):
    num = str(num)

    first = int(num[0])
    second = int(num[1])
    third = int(num[2])
    fourth = int(num[3])
    fifth = int(num[4])

    left_position = first + second
    right_position = fourth + fifth
    middle = third

    if left_position == right_position:
        print(num, end=' ')
    else:
        if left_position > right_position:
            right_position += middle

            if left_position == right_position:
                print(num, end=' ')
        else:
            left_position += middle

            if left_position == right_position:
                print(num, end=' ')

# equal sums (prime/ non-prime) ------------------------------------------------

num = input()
prime = 0
non_prime = 0

while num != 'stop':
    num = int(num)
    if num < 0:
        print(f'Number is negative.')
        num = input()
        continue

    is_not_prime = False

    for i in range(2, num):
        if num % i == 0:
            is_not_prime = True
            break

    if is_not_prime:
        non_prime += num
    else:
        prime += num
    num = input()

print(f'Sum of all prime numbers is: {prime}')
print(f'Sum of all non prime numbers is: {non_prime}')

# train the trainers -----------------------------------------------------------

jury = int(input())
presentation = input()
total_score = 0
total_avg_score = 0
presentation_count = 0

while not presentation == 'Finish':
    avg_score = 0  # nullify avg_score fpr every presentation
    total_score = 0

    for i in range(1, jury + 1):
        score = float(input())
        total_score += score
        total_avg_score += score
        presentation_count += 1

    avg_score = total_score / jury
    print(f'{presentation} - {avg_score:.2f}.')

    presentation = input()

else:
    total_avg_score /= presentation_count
    print(f"Student's final assessment is {total_avg_score:.2f}.")

# fishing ----------------------------------------------------------------------

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


# -----------------More Exercises-----------------------------------------------

# 01.unique pin codes-----------------------------------------------------------

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

# 05.challenge the wedding------------------------------------------------------

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

# 13.prime pairs----------------------------------------------------------------
