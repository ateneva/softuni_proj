
# **********************Lab ****************************************************

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


# ************************* Exercises ******************************************

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

# 03. football cards -----------------------------------------------------------

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

# 04. number beggars -----------------------------------------------------------

pool = input().split(", ")
beggars = int(input())

beggings = [0] * beggars  # determine the length of the list

for p in range(len(pool)):
    home = int(pool[p])
    turn = p % len(beggings)
    beggings[turn] += home

print(beggings)

# 05. faro shuffle -------------------------------------------------------------

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

# --------------06. survival of the biggest ------------------------------------

numbers = input().split(' ')
removals = int(input())

num = [int(n) for n in numbers]               # convert the list to integers
nums = sorted(num, reverse=True)[-removals:]  # find the smallest integers

for i in nums:
    if i in num:
        num.remove(i)
print(num)
