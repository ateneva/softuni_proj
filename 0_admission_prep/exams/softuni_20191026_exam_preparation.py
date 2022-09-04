
# ****************01.christmas sweets (simple operations and calculations) *****

baklava = float(input())
muffins = float(input())
stollen_kg = float(input())
sweets_kg = float(input())
biscuits_kg = float(input())

stollen = (baklava * 1.60) * stollen_kg
sweets = (muffins * 1.80 ) * sweets_kg
biscuits = biscuits_kg * 7.50

total = stollen + sweets + biscuits

print(f'{total:.2f}')


# ***************02.christmas market (condtional statements) *******************

import math as m

target = float(input())
fantasy_books = int(input())
horror_books = int(input())
romantic_books = int(input())

revenue = fantasy_books * 14.90 \
            + horror_books * 9.80 \
            + romantic_books * 4.30

taxed_revenue = revenue * 0.80

if taxed_revenue > target:
    earned = m.floor((taxed_revenue-target) * 0.10)
    print(f"{(taxed_revenue-earned):.2f} leva donated.")
    print(f"Sellers will receive {earned} leva.")
else:
    print(f"{target-taxed_revenue:.2f} money needed.")

# *************03.world snooker championship (nested condtionals) **************

stage = input()
ticket = input()
people = int(input())
snap = input()
price = 0

if stage == 'Quarter final':
    if ticket == 'Standard':
        price = 55.50

    elif ticket == 'Premium':
        price = 105.20

    elif ticket == 'VIP':
        price = 118.90

elif stage == 'Semi final':
    if ticket == 'Standard':
        price = 75.88

    elif ticket == 'Premium':
        price = 125.22

    elif ticket == 'VIP':
        price = 300.40

elif stage == 'Final':
    if ticket == 'Standard':
        price = 110.10

    elif ticket == 'Premium':
        price = 160.66

    elif ticket == 'VIP':
        price = 400

cost = price * people

if cost > 4000:
    cost *= 0.75

elif cost > 2500:
    if snap == 'Y':
        cost *= 0.90
        cost += (people * 40)
    else:
        cost *= 0.90

elif cost <= 2500:
    if snap == 'Y':
        cost += (people * 40)
    else:
        cost = cost

print(f'{cost:.2f}')

# *************04.bachelor party (while loop) **********************************

guest_fee = int(input())
people = input()                                  # all input is defined as string outside the loop and then converted to integer
meal_price = 0
total_meal_price = 0
total_people = 0

while not people == 'The restaurant is full':     # program should only end on input = 'The restaurant is full':
        people = int(people)
        if people < 5:
            meal_price += people * 100

        elif people >= 5:
            meal_price += people * 70

        total_people += people
        total_meal_price = meal_price

        people = input()                          # add strng input statement to ensure the loop ends

left = abs(total_meal_price - guest_fee)
if total_meal_price >= guest_fee:
    print(f'You have {total_people} guests and {left} leva left.')
else:
    print(f'You have {total_people} guests and {total_meal_price} leva income, but no singer.')


# *************05.movie ratings (for loop) *************************************

movies = int(input())
max_rating = 1
min_rating = 10
total_rating = 0
highest = ''
lowest = ''

for movie in range(movies):
    movie_title = input()
    rating = float(input())
    total_rating += rating

    if rating > max_rating:
        max_rating = rating
        highest = movie_title

    if rating < min_rating:
        min_rating = rating
        lowest = movie_title

    avg_rating = total_rating / movies

print(f"{highest} is with highest rating: {max_rating:.1f}")
print(f"{lowest} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {avg_rating:.1f}")

# ************06.christmas decoration (nested loop) ****************************

budget = int(input())
decoration = input()
money_left = 0
cost = 0

while decoration != 'Stop':
    for char in decoration:
        i = ord(char)
        cost += i

    if cost <= budget:
        print("Item successfully purchased!")
    else:
        print("Not enough money!")
        break

    money_left = abs(budget-cost)
    decoration = input()

else:
    print(f"Money left: {money_left}")
