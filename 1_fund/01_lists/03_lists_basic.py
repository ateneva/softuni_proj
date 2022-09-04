
# ***************************************** Lab ****************************************************

# 01. courses ---------------------------------
n = int(input())
courses = []

for n in range(n):
    course = input()
    courses.append(course)
print(courses)

# 02. strange zoo ------------------------------
tail = input()
body = input()
head = input()

meerkat = [tail, body, head]
meerkat[0], meerkat[2] = meerkat[2], meerkat[0]

animal = meerkat[::1]   # reverse the list

print(meerkat, animal)

# 03. lists statistics --------------------------

num = int(input())
positives = []
negatives = []
p = 0
n = 0

for num in range(num):
    i = int(input())
    if i > 0:
        positives.append(i)
        p += 1
    else:
        negatives.append(i)
        n += i
print(positives)
print(negatives)
print(f'Count of positives: {p}. Sum of negatives: {n}')

# 04. search ------------------------------------------------------

n = int(input())
word = input()
phrases = []

for i in range(n):
    phrase = input()
    phrases.append(phrase)

print(phrases)

for i in range(len(phrases) - 1, -1, -1):
    selection = phrases[i]
    if word not in selection:
        phrases.remove(selection)

print(phrases)

# 05. numbers filter -----------------------------------------------

n = int(input())
numbers = []
filtered = []

for i in range(n):
    number = int(input())
    numbers.append(number)

comm = input()

if comm == 'even':
    for number in numbers:
        if number % 2 == 0:
            filtered.append(number)

elif comm == 'odd':
    for number in numbers:
        if number % 2 != 0:
            filtered.append(number)

elif comm == 'negative':
    for number in numbers:
        if number < 0:
            filtered.append(number)

elif comm == 'positive':
    for number in numbers:
        if number >= 0:
            filtered.append(number)

print(filtered)


# ******************************************* Exercises *******************************************************

# 01. invert values -----------------------
string = input()
new = string.split()

opposite = []
for s in new:
    opp = int(s) * (-1)
    opposite.append(opp)

print(opposite)

# 02. multiple lists ----------------------
factor = int(input())
count = int(input())

l = []
x = 1

while len(l) < count:
    if x % factor == 0:
        l.append(x)
    x += 1

print(l)

# 03. football cards --------------------------------------------------------------------

cards = input().split(' ')

A = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
B = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

for card in cards:
    if card in A:
        A.remove(card)

    elif card in B:
        B.remove(card)

print(f"Team A - {len(A)}; Team B - {len(B)}")
if len(A) < 7 or len(B) < 7:
    print("Game was terminated")

# 04. number beggars --------------------------------------------------------------------

pool = input().split(", ")
beggars = int(input())

beggings = [0] * beggars  # determine the length of the list

for p in range(len(pool)):
    home = int(pool[p])
    turn = p % len(beggings)
    beggings[turn] += home

print(beggings)

# 05. faro shuffle -----------------------------------------------------------------------

cards = input().split(' ')
shuffles = int(input())

for c in range(shuffles):
    first_half = []
    second_half = []
    new_cards = []

    for fh in range(0, len(cards)// 2):
        first_half.append(cards[fh])

    for sh in range(len(cards) // 2, len(cards)):
        second_half.append(cards[sh])

    for i in range(len(first_half)):
        new_cards.append(first_half[i])
        new_cards.append(second_half[i])

    cards = new_cards

print(cards)

# ------------------------06. survival of the biggest ----------------------------------------------------------

numbers = input().split(' ')
removals = int(input())

num = [int(n) for n in numbers]               # convert the list to integers
nums = sorted(num, reverse=True)[-removals:]  # find the smallest integers

for i in nums:
    if i in num:
        num.remove(i)
print(num)

# ------------------------07. easter gifts (exam problem) ------------------------------------------------------

gifts = input().split(' ')
wish = input()

while wish != 'No Money':
    tokens = wish.split(' ')

    if tokens[0] == 'OutOfStock':
        gift = tokens[1]
        for g in range(len(gifts)):
            if gifts[g] == gift:
               gifts[g] = 'None'           # ideally we want to remove it from the list

    elif tokens[0] == 'Required':
        idx = int(tokens[2])
        if idx >= 0 and idx < len(gifts):  # check if the index is valid
            gifts[idx] = tokens[1]

    elif tokens[0] == 'JustInCase':
        gifts[-1] = tokens[1]              # replace the last present with the current present

    wish = input()

result = []
for gift in gifts:
    if gift != 'None':
        result.append(gift)

print(' '.join(result))

# ------------------------08. Seize the Fire (exam problem) ----------------------------------------------------

fires = input().split('#')
well = int(input())
effort = 0
cells = []

#print(fires)

for fire in fires:
    fire_type = fire.split('=')[0].strip()
    water = int(fire.split('=')[1])
    #print(fire_type, water)

    if well >= water:
        if fire_type == 'High':
            if water >= 81 and water <= 125:
                well -= water
                effort += water * 0.25
                cells.append(water)

        elif fire_type == 'Medium':
            if water >= 51 and water <= 80:
                well -= water
                effort += water * 0.25
                cells.append(water)

        elif fire_type == 'Low':
            if water >= 1 and water <= 50:
                well -= water
                effort += water * 0.25
                cells.append(water)

#print(cells)
print(f'Cells:')
for cell in cells:
    print(f'- {cell}')

print(f"Effort: {effort:.2f}")
print(f'Total Fire: {sum(cells)}')

# ------------------------09. Hello, France (exam problem) -----------------------------------------------------

items = input().split('|')
budget = float(input())
max_price = 0
earned = 0
spent = 0
bought = []

#print(items)

for item in items:
    clothing = item.split('->')[0]
    initial_price = float(item.split('->')[1])
    #print(clothing)
    #print(initial_price)

    if clothing == 'Clothes':
        max_price = 50

    elif clothing == 'Shoes':
        max_price = 35

    elif clothing == 'Accessories':
        max_price = 20.50

    if budget >= initial_price:
        if initial_price <= max_price:
            bought.append(initial_price)
            budget -= initial_price
            spent += initial_price

#print(bought)

for price in bought:
    price *= 1.40
    print(f'{price:.2f}', end=' ')
    earned += price

print()
#print(earned)
print(f'Profit: {earned-spent:.2f}')

if (earned + budget) >= 150:
    print("Hello, France!")
else:
    print("Time to go.")

# ------------------------10. Bread Factory (exam problem) -----------------------------------------------------

energy = 100
coins = 100
events = input().split('|')
completed = True

for event in events:
    activity = event.split('-')[0]
    number = int(event.split('-')[1])

    if activity == 'rest':
        if energy < 100:
            energy += number
            print(f"You gained {number} energy.")
        else:
            print(f"You gained {0} energy.")
        print(f"Current energy: {energy}.")

    elif activity == 'order':
        if (energy - 30) < 0:
            energy += 50
            print("You had to rest!")
        else:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")

    else:
        if (coins - number) > 0:
            print(f"You bought {activity}.")
            coins -= number
        else:
            print(f"Closed! Cannot afford {activity}.")
            completed = False
            break

if completed:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

# ******************************************* More Exercises ****************************************************
