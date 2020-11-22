

# ******************************************** 01.Easter Lunch (simple calculations) *******************************************************************

bakery = int(input())
eggs = int(input())
cookies = int(input())

bakery_cost = bakery * 3.20
eggs_cost = eggs * 4.35
cookies_cost = cookies * 5.40
paint_cost = eggs * 12 * 0.15

total = bakery_cost + eggs_cost + cookies_cost + paint_cost

print(f'{total:.2f}')

# ******************************************** 01.Easter Bakery (simple calculations) *******************************************************************

flour_price = float(input())
flour = float(input())
sugar = float(input())
eggs = int(input())
powder = int(input())

sugar_price = flour_price * 0.75

batter = flour * flour_price \
         + sugar * sugar_price \
         + eggs * (flour_price * 1.10) \
         + powder * (sugar_price * 0.20)

print(f'{batter:.2f}')

# ******************************************** 02.Easter Party (conditional statements) *****************************************************************

guests = int(input())
menu_price = float(input())
budget = float(input())

due = menu_price * guests

if guests >= 10 and guests <= 15:
    due *= 0.85

elif guests > 15 and guests <= 20:
    due *= 0.80

elif guests > 20:
    due *= 0.75

cake = budget * 0.10
total = due + cake

left = abs(budget - total)

if total <= budget:
    print(f"It is party time! {left:.2f} leva left.")
else:
    print(f"No party! {left:.2f} leva needed.")

# ******************************************** 02.Easter Guests (conditional statements) *****************************************************************

import math as m

guests = int(input())
budget = int(input())

pastry = m.ceil(guests / 3)
eggs = guests * 2

total = pastry * 4 + eggs * 0.45
left = abs(budget - total)

if total <= budget:
    print(f"Lyubo bought {pastry} Easter bread and {eggs} eggs.")
    print(f"He has {left:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {left:.2f} lv. more.")


# ******************************************** 03.Easter Trip (nested condtiinal statements) *************************************************************

destination = input()
period = input()
nights = int(input())
price = 0

if destination == 'France':
    if period == '21-23':
        price = 30

    elif period == '24-27':
        price = 35

    elif period == '28-31':
        price = 40

elif destination == 'Italy':
    if period == '21-23':
        price = 28

    elif period == '24-27':
        price = 32

    elif period == '28-31':
        price = 39

elif destination == 'Germany':
    if period == '21-23':
        price = 32

    elif period == '24-27':
        price = 37

    elif period == '28-31':
        price = 43

total = nights * price
print(f"Easter trip to {destination} : {total:.2f} leva.")

# ******************************************** 03.Painting Eggs (nested condtiinal statements) ***********************************************************

size = input()
colour = input()
number = int(input())
price = 0

if size == 'Large':
    if colour == 'Red':
        price = 16
    elif colour == 'Green':
        price = 12
    elif colour == 'Yellow':
        price = 9

elif size == 'Medium':
    if colour == 'Red':
        price = 13
    elif colour == 'Green':
        price = 9
    elif colour == 'Yellow':
        price = 7

elif size == 'Small':
    if colour == 'Red':
        price = 9
    elif colour == 'Green':
        price = 8
    elif colour == 'Yellow':
        price = 5

total = number * price * 0.65
print(f'{total:.2f} leva.')

# ******************************************** 04.Easter Eggs Battle (while loop) ************************************************************************

first_player = int(input())
second_player = int(input())
battle = input()                                 # define string input outside the loop
problems = 0

while not battle == 'End of battle':             # program shuld end on input = "End of Battle" or when 1 player is out of eggs

    if battle == 'one':
        second_player -= 1

    elif battle == 'two':
        first_player -= 1

    if first_player == 0:                        # check if player 1 has run out of eggs
        print(f"Player one is out of eggs. Player two has {second_player} eggs left.")
        break

    if second_player == 0:                       # check if player 2 has run out of eggs
        print(f"Player two is out of eggs. Player one has {first_player} eggs left.")
        break

    battle = input()                             # add string input statement to ensure the loop ends

else:
    print(f"Player one has {first_player} eggs left.")
    print(f"Player two has {second_player} eggs left.")

# ******************************************** 04.Easter Shop (while loop) *******************************************************************************

initial_volume = int(input())
activity = input()                             # define string input outside the loop
eggs_sold = 0

while not activity == 'Close':                 # program should end on input "Close" or when there are not enough eggs to sell
    eggs = int(input())                        # define the last intger/float input inside the loop 

    if activity == 'Buy':
        eggs_sold += eggs
        left = initial_volume
        initial_volume -= eggs

        if initial_volume < 0:                 # check if there are enough eggs to sell
            print("Not enough eggs in store!")
            print(f"You can buy only {left}.")
            break

    if activity == 'Fill':
        initial_volume += eggs

    activity = input()                         # add string input statement to avoid conversion issues and ensure the loop ends

else:
    print("Store is closed!")
    print(f"{eggs_sold} eggs sold.")


# ******************************************** 05.Easter Eggs (for loop) *********************************************************************************

eggs = int(input())
red = 0
orange = 0
blue = 0
green = 0

for egg in range(eggs):
    egg_colour = input()

    if egg_colour == 'red':
        red += 1

    elif egg_colour == 'orange':
        orange += 1

    elif egg_colour == 'blue':
        blue += 1

    elif egg_colour == 'green':
        green += 1

    max_eggs = max(red, orange, blue, green)

    if max_eggs == red:
        max_colour = "red"

    elif max_eggs == orange:
        max_colour = "orange"

    elif max_eggs == blue:
        max_colour = "blue"

    elif max_eggs == green:
        max_colour = "green"

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_eggs} -> {max_colour}")

# ******************************************** 05.Easter Bake (for loop) *********************************************************************************

import math as m

pastries = int(input())
sugar = 0
flour = 0
max_sugar = -10000
max_flour = -10000

for pastry in range(pastries):
    sugar_used = int(input())        # 950 gram per packet
    flour_used = int(input())        # 750 gram per packet

    sugar += sugar_used
    flour += flour_used

    sugar_needed = m.ceil(sugar/950)
    flour_needed = m.ceil(flour/750)

    if sugar_used > max_sugar:
        max_sugar = sugar_used

    if flour_used > max_flour:
        max_flour = flour_used

print(f"Sugar: {sugar_needed}")
print(f"Flour: {flour_needed}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")

# ******************************************** 06.Easter Competition (nested loop) ***********************************************************************

bakers = int(input())
max_points = 0
winner = ''

for b in range(bakers):
    baker = input()
    score = input()
    baker_points = 0

    while not score == 'Stop':
        score = int(score)
        baker_points += score
        score = input()

    else:
        print(f"{baker} has {baker_points} points.")
        if baker_points > max_points:
            max_points = baker_points
            winner = baker
            print(f"{winner} is the new number 1!")

print(f"{winner} won competition with {max_points} points!")


# ******************************************** 06.Easter Decoration (nested loop) ************************************************************************

customers = int(input())
total = 0

for customer in range(1, customers + 1):
    purchase = input()
    purchases = 0
    spent = 0

    while not purchase == 'Finish':
        purchases += 1

        if purchase == 'basket':
            spent += 1.50
        elif purchase == 'wreath':
            spent += 3.80
        elif purchase == 'chocolate bunny':
            spent += 7.00

        purchase = input()

    else:
        if purchases % 2 == 0:
            spent *= 0.80
        print(f"You purchased {purchases} items for {spent:.2f} leva.")

    total += spent
print(f"Average bill per client is: {total/customers:.2f} leva.")


