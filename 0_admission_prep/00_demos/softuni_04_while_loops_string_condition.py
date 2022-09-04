
# *************intger input with ending command string **************************

# -----Mock Exam 2019-10-27 bachelor party (while loops) -----------------------
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

# Input
# 2800
# 5
# 5
# 4
# 6
# 6
# 12
# 12
# The restaurant is full


# ********intger input with ending command string or integer *******************

# ---------------moving (practie problem)---------------------------------------

width = int(input())
length = int(input())
height = int(input())
boxes = input()                                # all input is defined as string outside the loop and then converted to integer
box_volume = 0
isFree = True

while not boxes == 'Done':                     # program should end on input "Done" or after there's no more free space
    boxes = int(boxes)
    box_volume += boxes

    if box_volume > (width * length * height): # check and break when there's no more free space
        isFree = False
        break

    boxes = input()                            # add strng input statement to ensure the loop ends

space_left = abs((width * length * height) - box_volume)
if isFree: # boolean take a value of true by default
    print(f'{space_left} Cubic meters left.')
else:
    print(f'No more free space! You need {space_left} Cubic meters more.')

# 10
# 10
# 2
# 20
# 20
# 20
# 20
# 122

# 10
# 1
# 2
# 4
# 6
# Done


# -----------------cake (practice problem)--------------------------------------
width = int(input())
length = int(input())
cake = input()                                   # all input is defined as string outside the loop and then converted to integer
slices = 0

while not cake == 'STOP':                        # program should end on input "STOP" or when we've run out of cake
    cake = int(cake)
    slices += cake

    if slices > width*length:                    # check and break when there is no more cake left
        left = abs(slices - width*length)
        print(f'No more cake left! You need {left} pieces more.')
        break

    cake = input()                               # add strng input statement to prevent conversion issues and ensure the loop ends

else:
    left = abs(slices - width*length)
    print(f'{left} pieces are left.')

# 10
# 10
# 20
# 20
# 20
# 20
# 21

# 10
# 2
# 2
# 4
# 6
# STOP

# ----------------diswasher (practice problem) ---------------------------------

bottles = int(input())
detergent = bottles * 750
cutlery = input()                                   # all input is defined as string outside the loop and then converted to integer
load = 0
used = 0
dishes = 0
pots = 0

while cutlery != 'End':                             # program should end when input = "End" or when we've run out of detergent
    cutlery = int(cutlery)
    load += 1

    if load % 3 == 0:
        used += int(cutlery) * 15
        pots += int(cutlery)

    else:
        used += int(cutlery) * 5
        dishes += int(cutlery)

    if used > detergent:                            # check if we've run out of detergent
        needed = abs(detergent - used)
        break

    cutlery = input()                               # add string input statement to avoid conversion issues and ensure the loop ends

if used <= detergent:
    print(f'Detergent was enough!')
    print(f'{dishes} dishes and {pots} pots were washed.')
    print(f'Leftover detergent {abs(detergent - used)} ml.')

else:
    print(f'Not enough detergent, {needed} ml. more necessary!')


# Input
# 2
# 53
# 65
# 55
# End

# Input
# 1
# 10
# 15
# 10
# 12
# 13
# 30

# ---------report system (practice problem)-------------------------------------

final_balance = int(input())
sales_price = input()                           # all input is defined as string outside the loop and then converted to integer
payment = 0
card = 0
cash = 0
card_sum = 0
cash_sum = 0
total_raised = 0

while not sales_price == 'End':                 # program should end when input = "End" or when enough money has been raised
    sales_price = int(sales_price)
    payment += 1

    if payment % 2 != 0:     # cash payment
        if sales_price > 100:
            print(f'Error in transaction!')
        else:
            print(f'Product sold!')
            cash_sum += sales_price
            cash += 1

    elif payment % 2 == 0:   # card payment
        if sales_price < 10:
            print(f'Error in transaction!')
        else:
            print(f'Product sold!')
            card_sum += sales_price
            card += 1

    total_raised = card_sum + cash_sum

    if total_raised >= final_balance:           # check if enough money has been raised
        print(f'Average CS: {cash_sum / cash:.2f}')
        print(f'Average CC: {card_sum / card:.2f}')
        break

    sales_price = input()                       # add string input statement to avoid conversion issues and ensure the loop ends

else:
    print(f'Failed to collect required money for charity.')

# 500
# 120
# 8
# 63
# 256
# 78
# 317

# 600
# 86
# 150
# 98
# 227
# End

# ---------Admission Exam 2019-06-15 cienma)-------------------------------------

hall_size = int(input())
cinema_goers = input()                                  # all string input is defined outside the loop and then converted to integer
capacity = hall_size
total_cinema_goers = 0
total_revenue = 0

while not cinema_goers == 'Movie time!':                # program should end on input 'Movie time!' or when the hall has reached capacity
    cinema_goers = int(cinema_goers)
    capacity -= cinema_goers

    if cinema_goers % 3 == 0:
        revenue = (cinema_goers * 5) - 5
    else:
        revenue = cinema_goers * 5

    total_cinema_goers += cinema_goers
    total_revenue += revenue

    if capacity < 0:                                    # check if the hall has reached capacity
        print(f"The cinema is full.")
        print(f"Cinema income - {total_revenue-revenue} lv.")
        break

    cinema_goers = input()                              # add string input statement to avoid conversion issues and ensure the loop ends

else:
    print(f"There are {capacity} seats left in the cinema.")
    print(f"Cinema income - {total_revenue} lv.")


# 60
# 10
# 6
# 3
# 20
# 15
# Movie time!

# 50
# 15
# 10
# 10
# 15
# 5

# 100
# 10
# 10
# 10
# 10
# 10
# 10
# 10
# 10
# 10
# 10
# Movie time!

# -------------------Admission exam 2019-07-07 Renovation ----------------------

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


# 3
# 5
# 10
# 2
# 3
# 4
# Tired!

# 2
# 3
# 25
# 6
# 7
# 8

# --------------------------------------------------------- syntax 2 ( Use a Boolean value )-----------------------------------------------------------------------=-

import math as m

height = int(input())
width = int(input())
excluded = int(input())
paint = input()                                            # all input is defined as string and then converted to integer
total_area = height * width * 4 * (1-excluded/100)
total_paint = 0
is_painted = False

while not paint == 'Tired!':                               # program should end on input = "Tired!" or when all surface has been painted
    paint = int(paint)
    total_paint += paint
    painted_area = total_area - total_paint

    if painted_area <= 0:                                  # check if all surface has been covered
        is_painted = True
        break

    paint = input()                                        # add a string input to make sure the loop ends

if not is_painted:
    print(f"{m.floor(painted_area)} quadratic m left.")

else:
    if painted_area < 0:
        print(f"All walls are painted and you have {m.floor(abs(painted_area))} l paint left!")
    else:
        print(f"All walls are painted! Great job, Pesho!")


# 3
# 5
# 10
# 2
# 3
# 4
# Tired!

# 2
# 3
# 25
# 6
# 7
# 8


# ---------------syntax 3 (just break and print all output in the end ----------
import math as m

height = int(input())
width = int(input())
excluded = int(input())
paint = input()                                             # all input is defined as string and then converted to integer
total_area = height * width * 4 * (1-excluded/100)

while not paint == 'Tired!':                                # program should end on input = "Tired!" or when all surface has been painted
    paint = int(paint)
    total_area -= paint

    if total_area <= 0:                                     # check if all surface has been painted
        break

    paint = input()                                         # add a string input to make sure the loop ends

if total_area > 0:
    print(f"{m.floor(total_area)} quadratic m left.")

elif total_area == 0:
    print(f"All walls are painted! Great job, Pesho!")

elif total_area < 0:
    print(f"All walls are painted and you have {m.floor(abs(total_area))} l paint left!")


# 3
# 5
# 10
# 2
# 3
# 4
# Tired!

# 2
# 3
# 25
# 6
# 7
# 8



# **********string input with ending command string ****************************

# -------------Admission Exam 2019-04-07 (cinema voucher)-----------------------
voucher = int(input())
purchase = input()                                # define string input outside the loop
tickets = 0
others = 0

while not purchase == 'End':                      # program should end on input = 'End' oe when there's no more money on the voucher
    if len(purchase) > 8:
        price = ord(purchase[0]) + ord(purchase[1])
        if price <= voucher:
            tickets += 1
    else:
        price = ord(purchase[0])
        if price <= voucher:
            others += 1

    voucher -= price
    if voucher < 0:                               # check for the voucher remaining balance
        break

    purchase = input()                            # add string input statement to ensure that the loop ends

print(tickets)
print(others)

# 300
# Captain Marvel
# popcorn
# Pepsi

# 1500
# Avengers: Endgame
# Bohemian Rhapsody
# Deadpool 2
# End

# ------------Admission Exam 2019-04-21 (Easter Eggs Battle)--------------------

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


# 5
# 4
# one
# two
# one
# two
# two
# End of battle

# 2
# 6
# one
# two
# two

# 6
# 3
# one
# two
# two
# one
# one


# *************************************************integer and string input with ending command string or integer ***************************************************

# --------------------------------------------------------exam preparation (practice problem)------------------------------------------------------------------------

fail_grades = int(input())
problem = input()                                # define string input outside the loop
problems = 0
grades = 0
fail_grades_counter = 0
last_problem = 'None'

while not problem == 'Enough':                   # program should on input = 'Enough' or upon receiving all possible fail grades

    grade = int(input())                         # define the last integer/float input inside the loop
    grades += grade
    problems += 1
    last_problem = problem

    if grade <= 4:
        fail_grades_counter += 1
        if fail_grades_counter == fail_grades:   # check if the maximum number of fail grades has been reached
            break

    problem = input()                            # add string input statement to avoid conversion issues and ensure the loop ends

if fail_grades_counter == fail_grades:
    print(f'You need a break, {fail_grades} poor grades.')

else:
    avg_score = grades / problems
    print(f'Average score: %.2f' % avg_score)
    print(f'Number of problems: {problems}')
    print(f'Last problem: {last_problem}')


# 3
# Money
# 6
# Story
# 4
# Spring Time
# 5
# Bus
# 6
# Enough

# 2
# Income
# 3
# Game Info
# 6
# Best Player
# 4

# -------------------------------------------------------Admission Exam 2019-07-28 (best plane tickets) ---------------------------------------------------------------

ticket = input()
min_delay = 501

while not ticket == 'End':
    price = float(input())            # define the last intger/float input inside the loop
    delay = int(input())              # define the last intger/float input inside the loop

    if delay < min_delay:
        min_delay = delay
        last_ticket = ticket
        last_price = price * 1.96
        hours = (delay // 60)
        minutes = delay % 60

    ticket = input()

else:
    print(f"Ticket found for flight {last_ticket} costs {last_price:.2f} leva with {hours}h {minutes}m stay")

# W64301
# 60
# 140
# FR9967
# 80
# 200
# FR0066
# 45
# 60
# End

# W64301
# 60
# 140
# W30510
# 110
# 40
# W51440
# 160
# 70
# FR0066
# 75
# 75
# End

# W43122
# 30
# 120
# W35400
# 30
# 100
# End

# -------------------------------------------------------Admission Exam 2019-07-28 (darts tournament) -----------------------------------------------------------------

initial_score = int(input())
score_range = input()                             # define string input outside the loop
moves = 0

while not score_range == 'bullseye':              # program should end when someone hits the bullseye
    score = int(input())                          # define the last intger/float input inside the loop
    moves += 1

    if score_range == 'number section':
        initial_score -= score

    elif score_range == 'double ring':
        initial_score -= score * 2

    elif score_range == 'triple ring':
        initial_score -= score * 3

    if initial_score == 0:                        # check if a player has won by reaching 0 points
        print(f'Congratulations! You won the game in {moves} moves!')
        break

    if initial_score < 0:                         # check if a player has lost
        print(f"Sorry, you lost. Score difference: {abs(initial_score)}.")
        break

    score_range = input()                         # add string input statement to avoid conversion issues and to ensure the loop ends

else:
    print(f'Congratulations! You won the game with a bullseye in {moves+1} moves!')

# 150
# double ring
# 20
# triple ring
# 10
# number section
# 20
# triple ring
# 20

# 101
# triple ring
# 7
# double ring
# 19
# bullseye

# 75
# triple ring
# 17
# number section
# 16
# triple ring
# 13
# double ring
# 10

# -------------------------------------------------------Admission Exam 2019-07-07 (club) -----------------------------------------------------------------------------

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

# 100
# Sidecar
# 7
# Mojito
# 5
# White Russian
# 10

# 500
# Bellini
# 6
# Bamboo
# 7
# Party!

# --------------------------------------------------------Admission Exam 2019-06-15 (movie stars)--------------------------------------------------------------------

budget = float(input())
actor = input()                                 # define string input outside the loop

while not actor == 'ACTION':                    # program should end with ACTION or when budget has reached 0

    if len(actor) <= 15:
        salary = float(input())                 # define the last intger/float input inside the loop

    else:
        salary = budget * 0.20

    budget -= salary

    if budget <= 0:                             # check if budget has been exhausted
        print(f"We need {abs(budget):.2f} leva for our actors.")
        break

    actor = input()                             # add string input statement to avoid conversion issues and ensure the loop ends

else:
    print(f"We are left with {budget:.2f} leva.")


# 90000
# Christian Bale
# 70000.50
# Leonard DiCaprio
# Kevin Spacey
# 24000.99

# 170000
# Ben Affleck
# 40000.50
# Zahari Baharov
# 80000
# Tom Hanks
# 2000.99
# ACTION


# -------------------------------------------------------Admission Exam 2019-05-03 (tourist shop)-----------------------------------------------------------------

budget = float(input())
product = input()                              # define string input outside the loop
orders = 0
total_price = 0

while not product == 'Stop':                   # program should end with ACTION or when price is greater than remaining budget
    price = float(input())                     # define the last intger/float input inside the loop
    orders += 1

    if orders % 3 == 0:
        price /= 2
    else:
        price

    budget -= price
    total_price += price

    if (budget - price) <= 0:                  # check if budget has been exhausted
        print(f"You don't have enough money!")
        print(f"You need {abs(budget):.2f} leva!")
        break

    product = input()                          # add string input statement to avoid conversion issues and ensure the loop ends

else:
    print(f"You bought {orders} products for {total_price:.2f} leva.")


# 153.20
# Backpack
# 25.20
# Shoes
# 54
# Sunglasses
# 30
# Stop

# 54
# Thermal underwear
# 24
# Sunscreen
# 45

# -----------------------------------------------------Admission Exam 2019-04-21 (Easter Shop)---------------------------------------------------------------------

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


# 13
# Buy
# 8
# Fill
# 3
# Buy
# 10

# 20
# Fill
# 30
# Buy
# 15
# Buy
# 20
# Close

# -----------------------------------------------------Admission Exam 2019-03-10 (darts)---------------------------------------------------------------------

player = input()
field = input()                                # define the string input outside the loop
score = 301
success = 0
fail = 0

while not field == 'Retire':                   # program should end on input "Retire" or when points reach 0
    points = int(input())                      # define the last intger/float input inside the loop

    if field == 'Single':
        if points <= score:
            success += 1
            score -= points
        else:
            fail += 1

    elif field == 'Double':
        if (points * 2) <= score:
            success += 1
            score -= (points * 2)
        else:
            fail += 1

    elif field == 'Triple':
        if (points * 3) <= score:
            success += 1
            score -= (points * 3)
        else:
            fail += 1

    if score == 0:                             # check if final score has reached 0
        print(f"{player} won the leg with {success} shots.")
        break

    field = input()                            # add string input statement to avoid conversion issues and ensure the loop ends

else:
    print(f"{player} retired after {fail} unsuccessful shots.")

# Michael van Gerwen
# Triple
# 20
# Triple
# 19
# Double
# 10
# Single
# 3
# Single
# 1
# Triple
# 20
# Triple
# 20
# Double
# 20

# Stephen Bunting
# Triple
# 20
# Triple
# 20
# Triple
# 20
# Triple
# 20
# Triple
# 20
# Triple
# 20
# Double
# 7
# Single
# 12
# Double
# 1
# Single
# 1

# Rob Cross
# Triple
# 20
# Triple
# 20
# Triple
# 20
# Triple
# 20
# Double
# 20
# Triple
# 20
# Double
# 5
# Triple
# 10
# Double
# 6
# Retire

# -----------------------------------------------------Admission Exam 2019-03-10 (number wars)---------------------------------------------------------------------
first_player = input()
second_player = input()
first = input()                             # define first player points as string input outside the loop
first_points = 0
second_points = 0

while first != 'End of game':               # program should end on "End of game or when there was a number war"
    first = int(first)
    second = int(input())                   # define the last intger/float input inside the loop

    if first > second:
        first_points += (first-second)

    elif first < second:
        second_points += (second-first)

    elif first == second:                   # check the outcome of a number war
        first = int(input())
        second = int(input())

        if first > second:
            winner = first_player
            points = first_points
        else:
            winner = second_player
            points = second_points
        print(f"Number wars!")
        print(f"{winner} is winner with {points} points")
        break

    first = input()                        # add string input statement for the first points to avoid conversion issues and to ensure the loop ends

else:
    print(f"{first_player} has {first_points} points")
    print(f"{second_player} has {second_points} points")


# Desi
# Niki
# 7
# 5
# 3
# 4
# 3
# 3
# 5
# 3

# Elena
# Simeon
# 6
# 3
# 2
# 5
# 8
# 9
# End of game

# Aleks
# Georgi
# 4
# 5
# 3
# 2
# 4
# 3
# 4
# 4
# 5
# 2

# ------------------------------------------------------------stream of letters (practice problme)--------------------------------------------------------------------

letter = input()
output = ''
c_found = False
o_found = False
n_found = False
current_word = ''

while not letter == 'End':
    ascii_char = ord(letter)
    upper_case = ascii_char >= 65 and ascii_char <= 90
    lower_case = ascii_char >= 97 and ascii_char <= 122

    if upper_case or lower_case:

        if letter == 'c' and not c_found:
            c_found = True
            letter = input()
            if c_found and o_found and n_found:
                output += f'{current_word} '
                current_word = ''
                c_found = False
                o_found = False
                n_found = False
            continue   # skip to the following iteration

        if letter == 'o' and not o_found:
            o_found = True
            letter = input()
            if c_found and o_found and n_found:
                output += f'{current_word} '
                current_word = ''
                c_found = False
                o_found = False
                n_found = False
            continue

        if letter == 'n' and not n_found:
            n_found = True
            letter = input()
            if c_found and o_found and n_found:
                output += f'{current_word} '
                current_word = ''
                c_found = False
                o_found = False
                n_found = False
            continue

        current_word += letter

    letter = input()

print(output)
