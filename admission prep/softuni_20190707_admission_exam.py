
 # ******************************************** 01.pool day (simple calculations) ***************************************************************

import math as m

people = int(input())
admission = float(input())
chaizlongue = float(input())
umbrella = float(input())

admissions = admission * people
chaizlongues = m.ceil(people * 0.75) * chaizlongue
umbreallas = m.ceil(people * 0.50) * umbrella

needed = admissions + chaizlongues + umbreallas
print(f"{needed:.2f} lv.")

 # ******************************************** 01.repainting (simple calculations) *************************************************************

naylone = int(input())
paint = int(input())
dilution = int(input())
labour = int(input())

naylone_cost = (naylone + 2) * 1.50
paint_cost = (paint + paint*0.10) * 14.50
dilution_cost = dilution * 5.00

labour_cost = (naylone_cost + paint_cost + dilution_cost + 0.40) * 0.30
labour_cost = labour_cost * labour

total_cost = (naylone_cost + paint_cost + dilution_cost + 0.40) + labour_cost

print(f"Total expenses: {total_cost:.2f} lv.")

 # ******************************************** 02.family trip (conditional statements) *********************************************************

budget = float(input())
nights = int(input())
price_per_night = float(input())
unallocated = int(input())

if nights > 7:
    price = price_per_night * 0.95
else:
    price = price_per_night

misc = budget * (unallocated/100)
expenses = (nights * price) + misc

left = abs(expenses-budget)

if expenses <= budget:
    print(f"Ivanovi will be left with {left:.2f} leva after vacation.")

else:
    print(f"{left:.2f} leva needed.")

 # ******************************************** 02.shopping (conditional statements) ************************************************************

budget = float(input())
videocard = int(input())
processor = int(input())
RAM = int(input())

videocards = videocard * 250
processors = processor * (videocards * 0.35)
RAMs = RAM * (videocards * 0.10)

cost = videocards + processors + RAMs

if videocard > processor:
    cost = cost * 0.85
else:
    cost = cost

left = abs(budget - cost)

if cost <= budget:
    print(f"You have {left:.2f} leva left!")
else:
    print(f"Not enough money! You need {left:.2f} leva more!")

 # ******************************************** 03.coffee machine (nested condtiinal statements) ************************************************

drink = input()
sugar = input()
bought = int(input())
price = 0
discount = 0

if drink == 'Espresso':
    if sugar == 'Without':
        price = 0.90 * (1-0.35)
    elif sugar == 'Normal':
        price = 1.00
    elif sugar == 'Extra':
        price = 1.20

    if bought >= 5:
        discount = bought * price * 0.25

elif drink == 'Cappuccino':
    if sugar == 'Without':
        price = 1.00 * (1-0.35)
    elif sugar == 'Normal':
        price = 1.20
    elif sugar == 'Extra':
        price = 1.60

elif drink == 'Tea':
    if sugar == 'Without':
        price = 0.50 * (1-0.35)
    elif sugar == 'Normal':
        price = 0.60
    elif sugar == 'Extra':
        price = 0.70

total_price = (bought * price) - discount
if total_price > 15:
    total_price *= 0.80

print(f"You bought {bought} cups of {drink} for {total_price:.2f} lv.")

 # ******************************************** 03.travel agency (nested condtiinal statements) *************************************************

city = input()
package = input()
VIP = input()
days = int(input())
price = 0
discount = 0

if city not in ('Bansko','Borovets','Varna', 'Burgas'):
    print("Invalid input!")

elif package not in ('withEquipment', 'noEquipment', 'withBreakfast', 'noBreakfast'):
    print("Invalid input!")

elif days <= 0:
    print("Days must be positive number!")

elif days > 0:
    if city == 'Bansko' or city == 'Borovets':
        if package == 'withEquipment':
            price = 100
            discount = 0.10
        elif package == 'noEquipment':
            price = 80
            discount = 0.05

    elif city == 'Varna' or city == 'Burgas':
        if package == 'withBreakfast':
            price = 130
            discount = 0.12
        elif package == 'noBreakfast':
            price = 100
            discount = 0.07

    if days > 7:
        days = days - 1

    if VIP == 'yes':
        total_price = days * price * (1-discount)
    else:
        total_price = days * price

    print(f"The price is {total_price:.2f}lv! Have a nice time!")

 # ******************************************** 04.club (while loop) ****************************************************************************

target_revenue = float(input())
cocktail = input()                               # define string input outside the loop
revenue = 0
order_revenue = 0

while not cocktail == 'Party!':                  # program should end when input = "Party" or target revenue has been reached

    order = int(input())                         # define the last intger/float input inside the loop 
    order_revenue = int(len(cocktail)) * order

    if order_revenue % 2 == 0:
        revenue += order_revenue
    else:
        revenue += order_revenue * 0.75

    if revenue >= target_revenue:                # check if target revenue has been reached
        print(f"Target acquired.")
        print(f"Club income - {revenue:.2f} leva.")
        break

    cocktail = input()                           # add string input statement to avoid conversion issues and ensure the loop ends

else:
    print(f"We need {abs(target_revenue - revenue):.2f} leva more.")
    print(f"Club income - {revenue:.2f} leva.")


 # ******************************************** 04.renovation (while loop) **********************************************************************

import math as m

height = int(input())
width = int(input())
excluded = int(input())
paint = input()                                          # all input is defined as string and then converted to integer
total_area = height * width * 4 * (1-excluded/100)

while not paint == 'Tired!':                             # program should end on input = "Tired!" or when all surface has been painted
    paint = int(paint)
    total_area -= paint

    if total_area < 0:
        print(f"All walls are painted and you have {m.floor(abs(total_area))} l paint left!")
        break

    elif total_area == 0:
        print(f"All walls are painted! Great job, Pesho!")
        break

    paint = input()                                      # add a string input to make sure the loop ends

else:
    print(f"{m.floor(total_area)} quadratic m left.")


 # ******************************************** 05.pc game shop (for loop) **********************************************************************

games_sold = int(input())
heartstone = 0
fornite = 0
overwatch = 0
others = 0

for game in range(games_sold):
    game_title = input()

    if game_title == 'Hearthstone':
        heartstone += 1

    elif game_title == 'Fornite':
        fornite += 1

    elif game_title == 'Overwatch':
        overwatch += 1

    else:
        others += 1

print(f"Hearthstone - {heartstone/games_sold*100:.2f}%")
print(f"Fornite - {fornite/games_sold*100:.2f}%")
print(f"Overwatch - {overwatch/games_sold*100:.2f}%")
print(f"Others - {others/games_sold*100:.2f}%")

 # ******************************************** 05.football tournament (for loop) ***************************************************************

team = input()
games = int(input())
game_count = 0
wins = 0
d = 0
losses = 0
points = 0

for game in range(games):
    outcome = input()
    game_count += 1

    if outcome == 'W':
        wins += 1
        points += 3

    elif outcome == 'D':
        d += 1
        points += 1

    else:
        losses += 1

    win_rate = wins/game_count*100

if games > 0:
    print(f"{team} has won {points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {d}")
    print(f"## L: {losses}")
    print(f"Win rate: {win_rate:.2f}%")

else:
    print(f"{team} hasn't played any games during this season.")

 # ******************************************** 06.name game (nested loop) **********************************************************************

player = input()
winner_points = 0
winner = ''

while player != 'Stop':
    points = 0

    for char in player:
        i = ord(char)
        num = int(input())

        if i == num:
            points += 10
        else:
            points += 2

    if points >= winner_points:
        winner_points = points
        winner = player

    player = input()

print(f"The winner is {winner} with {winner_points} points!")

 # ******************************************** 06.the most powerful word (nested loop) *********************************************************

word = input()
strongest = 0
most_powerful_word = ''

while word != 'End of words':
    strength = 0

    for char in word:
        i = ord(char)
        strength += i

    if word[0] in ('a', 'e', 'i', 'o', 'u', 'y') \
        or word[0] in ('A', 'E', 'I', 'O', 'U', 'Y'):
        strength *= len(word)

    else:
        strength //= len(word)

    if strength >= strongest:
        strongest = strength
        most_powerful_word = word

    word = input()

print(f"The most powerful word is {most_powerful_word} - {strongest}")