
# *****************Lab ********************************

# the biggest number ------------------------------
a = int(input())
b = int(input())
c = int(input())

max_num = max(a, b, c)
print(max_num)

# number definer ----------------------------------
num = float(input())

if num == 0:
    print("zero")

elif abs(num) < 1:
    if num > 0:
        print("small positive")
    else:
        print('small negative')

elif abs(num) >= 1000000:
    if num > 0:
        print("large positive")
    else:
        print("large negative")

elif num > 0:
    print("positive")

else:
    print('negative')

# reversed word ------------------------------------------
word = input()
reversed_word = ''

for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]

print(reversed_word)

# number between 1 and 100 --------------------------------

num = 0.0
while num < 1 or num > 100:
    num = float(input())

else:
    print(f'The number {num} is between 1 and 100')

# patterns ------------------------------------------------

num = int(input())

for i in range(1, num + 1):
    for j in range(0, i):
        print('*', end='')
    print()

# creating the reversed pattern
for i in range(num - 1, 0, -1):
    for j in range(0, i):
        print('*', end='')
    print()

# *****************Exercises ***************************************************

# 01. Jenny's Secret Message --------------------------------
name = input()

if name == 'Johnny':
    print('Hello, my love!')

else:
    print(f'Hello, {name}!')

# 02. Drink Something ---------------------------------------

age = int(input())

if age <= 14:
    print("drink toddy")

elif age > 14 and age <= 18:
    print("drink coke")

elif age > 18 and age <= 21:
    print("drink beer")

else:
    print("drink whisky")

# 03. Leonardo DiCaprio's Oscars -----------------------------

year = int(input())

if year == 88:
    print("Leo finally won the Oscar! Leo is happy")

elif year == 86:
    print("Not even for Wolf of Wall Street?!")

elif year > 88:
    print("Leo got one already!")

else:
    print("When will you give Leo an Oscar?")

# 04. Double Char ------------------------------------------
phrase = input()
word = ''

for w in phrase:
   word += str(w) * 2
print(word)

# 05. Can't Sleep? Count Sheep -----------------------------
sheep = int(input())
count = 0

for sh in range(1, sheep + 1):
    count += 1
    print(f'{count} sheep...', end='')

# 06. Next Happy Year ---------------------------------------
year = input()

while True:
    year = str(int(year) + 1)
    set(year)  # returns the unique values within a string

    if len(set(year)) == len(year):
        print(year)
        break

# 07. Maximum Multiple ---------------------------------------
divisor = int(input())
bound = int(input())
num = 0

for i in range(bound, 0, -1):  # reversed range
    if i % divisor == 0:
        num = i
        break
print(num)
