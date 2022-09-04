
# ******************************************* Lab **************************************************

# 01. concat names ---------------------------
name = input()
surname = input()
delimiter = input()

print(f'{name}{delimiter}{surname}')

# 02. centuries to minutes --------------------------------------------------------------------
cent = int(input())
years = cent * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60

print(f'{cent} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')

# 03. special numbers ---------------------------------------------------------------------------
num = int(input())

for i in range(1, num + 1):
    sum_of_digits = 0
    digits = i

    while digits > 0:
        sum_of_digits += digits % 10
        digits = int(digits/10)

    if (sum_of_digits == 5) or (sum_of_digits == 7) or (sum_of_digits == 11):
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')

# 04. convert meters to centimeters --------------------------------------------------------------
meters = int(input())

kilometers = meters * 0.001
print(f'{kilometers:.2f}')

# 05. pound to dollars ---------------------------------------------------------------------------
pounds = int(input())

dollars = pounds * 1.31
print(f'{dollars:.3f}')

# ******************************************* Exercises *******************************************************

# 01. integer operations ----------------------------------
a = int(input())
b = int(input())
c = int(input())
d = int(input())

x = int((a + b ) / c) * d
print(x)

# 02. chars to string -------------------------------------
a = input()
b = input()
c = input()

print(f'{a}{b}{c}')

# 03. elevator --------------------------------------------

people = int(input())
capacity = int(input())

full = people // capacity
remainder = people % capacity
course = full

if remainder > 0:
    course = full + 1

print(course)

# 04. sum of chars ----------------------------------------
n = int(input())
count = 0
char_value = 0

while count < n:
    char = input()
    char_value += ord(char)
    count += 1

print(f'The sum equals: {char_value}')

# 05. print part of the ASCII table -----------------------
start = int(input())
end = int(input())

for i in range(start, end + 1):
    print(chr(i), end=' ')

# 06. triples of Latin letters ----------------------------

n = int(input())

for i in range(97, 97 + n):
    for j in range(97, 97 + n):
        for k in range(97, 97 + n):
            print(f'{chr(i)}{chr(j)}{chr(k)}')

# 07. water overflow --------------------------------------
iter = int(input())
count = 0
full = 0

while count < iter:
    litres = int(input())
    full += litres
    count += 1

    if full > 255:
        print("Insufficient capacity!")
        full -= litres
        continue

print(f'{full}')

# ----------------------------08. party profit (exam problem) ----------------------------------------
party_size = int(input())
days = int(input())
earned = 0

for day in range(1, days + 1):
    earned += 50

    if day % 10 == 0:
        party_size -= 2

    if day % 15 == 0:
        party_size += 5

    if day % 3 == 0:
        earned -= party_size * 3  # spent on drinking water every 3rd day

    if day % 5 == 0:
        earned += party_size * 20 # earn for slaying a monster every 5th day

        if day % 3 == 0:
            earned -= party_size * 2

    earned -= party_size * 2      # spent on food every day

    # earned must be at the end of each statements, so that party size is picked up correctly

print(f"{party_size} companions received {earned // party_size} coins each.")

# -----------------------------09. snowballs (exam problme) --------------------------------------------------

snowballs = int(input())
MaxSnowballValue = 0

MaxSnowBallSnow = 0
MaxSnowBallTime = 0
snowballValue = 0
MaxSnowBallQuality = 0

for snowball in range(1, snowballs + 1):
    snowballSnow = int(input())
    snowballTime = int(input())
    snowballQuality = int(input())

    snowballValue = int(snowballSnow / snowballTime) ** snowballQuality

    if snowballValue > MaxSnowballValue:
        MaxSnowballValue = snowballValue
        MaxSnowBallSnow = snowballSnow
        MaxSnowBallTime = snowballTime
        MaxSnowBallQuality = snowballQuality

print(f'{MaxSnowBallSnow} : {MaxSnowBallTime} = {MaxSnowballValue} ({MaxSnowBallQuality})')

# -----------------------------10. gladiator expenses (exam problem) -----------------------------------------
lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armour_price = float(input())
expenses = 0

for l in range(1, lost_fights + 1):

    if l % 2 == 0:
        expenses += helmet_price

    if l % 3 == 0:
        expenses += sword_price

    if l % 6 == 0:
        expenses += shield_price

    if l % 12 == 0:
        expenses += armour_price

print(f"Gladiator expenses: {expenses:.2f} aureus")

# ******************************************* More Exercises **************************************************

# 01. biggest of the three numbers ---------------------------
x = int(input())
y = int(input())
z = int(input())

output = max(x, y, z)
print(output)

# 02. exchange integers --------------------------------------

a = int(input())
b = int(input())
print('Before:')
print(f"a = {a} \nb = {b}")

temp = a
a = b
b = temp
print('After:')
print(f"a = {a} \nb = {b}")

# 03. prime number checker -----------------------------------

import math
num = int(input())
primeNum = True
sqrRt = math.floor(math.sqrt(num))
counter = 0

for i in range(2, sqrRt + 1):
    if num % i == 0:
        counter += 1
if counter > 0:
    primeNum = False
print(primeNum)

# 04. decrypting messages ------------------------------------
key = int(input())
lines = int(input())
decoded = ''

for l in range(1, lines + 1):
    char = input()
    decoded_char = chr(key + ord(char))
    decoded += decoded_char

print(decoded, end='')

# 05. balanced brackets --------------------------------------
count = int(input())
balance = True
open = False

for i in range(0, count):
    data = input()
    if data == "(":
        if (not open):
            open = True
        else:
            balance = False
    if data == ")":
        if open:
            open = False
        else:
            balance = False

if balance and not open:
    print("BALANCED")
else:
    print("UNBALANCED")

