
 # ******************************************** 01.savings (simple calculations) *************************************************************

income = float(input())
months = int(input())
expenses = float(input())

unforeseen = income * 0.30

savings = income - (expenses + unforeseen)
total_savings = months * savings
percent = savings / income * 100

print(f"She can save {percent:.2f}%")
print(f"{total_savings:.2f}")

 # ******************************************** 01.lemonade stand (simple calculations) ******************************************************

lemons = float(input())
sugar = float(input())
water = float(input())

juice = lemons * 980
lemonade = juice + (water * 1000) + (sugar * 0.7)
cups = round(lemonade // 150)
earned = cups * 1.20

print(f"All cups sold: {cups}")
print(f"Money earned: {earned:.2f}")

 # ******************************************** 02.reservaton (conditional statements) *******************************************************

book_date = int(input())
book_month = int(input())
arrival_date = int(input())
arrival_month = int(input())
departure_date = int(input())
departure_month = int(input())

nights = departure_date - arrival_date

if book_month < arrival_month:
    price = 25
    payable = nights * price * 0.80

elif (arrival_date - book_date) >= 10:
    price = 25
    payable = nights * price

else:
    price = 30
    payable = nights * price

print(f"Your stay from {arrival_date}/{arrival_month} to {departure_date}/{departure_month} will cost {payable:.2f}")


 # ******************************************** 02.summer shopping (condtiinal statements) ***************************************************

budget = float(input())
towel = float(input())
discount = int(input())

umbrella = (2/3) * towel
flops = umbrella * 0.75
bag = (towel + flops) * 1/3

payable = (towel + umbrella + flops + bag) * (1-discount/100)
left = abs(payable - budget)

if payable <= budget:
    print(f"Annie's sum is {payable:.2f} lv. She has {left:.2f} lv. left.")
else:
    print(f"Annie's sum is {payable:.2f} lv. She needs {left:.2f} lv. more.")

 # ******************************************** 03.luggage tax (nested condtional statements) ************************************************

height = int(input())
width = int(input())
length = int(input())
ticket = input()
tax = 0

size = height * width * length

if ticket == 'true':
    if size >= 50 and size <= 100:
        tax = 0

    elif size > 100 and size <= 200:
        tax = 10

    elif size > 200 and size <= 300:
        tax = 20

elif ticket == 'false':
    if size >= 50 and size <= 100:
        tax = 25

    elif size > 100 and size <= 200:
        tax = 50

    elif size > 200 and size <= 300:
        tax = 100

print(f"Luggage tax: {tax:.2f}")

 # ******************************************** 03.cruise ship (nested condtiional statements) ***********************************************

cruise = input()
cabin = input()
nights = int(input())
people = 4
price = 0

if cruise == 'Mediterranean':
    if cabin == 'standard cabin':
        price = 27.50

    elif cabin == 'cabin with balcony':
        price = 30.20

    elif cabin == 'apartment':
        price = 40.50

elif cruise == 'Adriatic':
    if cabin == 'standard cabin':
        price = 22.99

    elif cabin == 'cabin with balcony':
        price = 25.00

    elif cabin == 'apartment':
        price = 34.99

elif cruise == 'Aegean':
    if cabin == 'standard cabin':
        price = 23.00

    elif cabin == 'cabin with balcony':
        price = 26.60

    elif cabin == 'apartment':
        price = 39.80

if nights > 7:
    cost = nights * price * people * 0.75
else:
    cost = nights * price * people

print(f"Annie's holiday in the {cruise} sea costs {cost:.2f} lv.")


 # ******************************************** 04.best plane tickets (while loop) ***********************************************************

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


 # ******************************************** 04.darts tournament (while loop) *************************************************************

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


 # ************************************************ 05.seats (for loop) **********************************************************************

 tickets = int(input())

for ticket in range(tickets):
    ticket_num = input()

    if len(ticket_num) >= 5:
        decoded_ticket = ticket_num[0] + str(ord(ticket_num[1]))

    elif ord(ticket_num[0]) >=65 and ord(ticket_num[0]) <= 90:
        decoded_ticket = ticket_num[0] + ticket_num[1] + ticket_num[2]

    else:
        decoded_ticket = ticket_num[3] + ticket_num[1] + ticket_num[2]

    print(f'Seat decoded: {decoded_ticket}')


 # ************************************************ 05.cruise games (for loop) ***************************************************************

import math as m

player = input()
games = int(input())
volleyball_score = 0
tennis_score = 0
badminton_score = 0
volleyball = 0
tennis = 0
badminton = 0

for game in range(games):
    game_name = input()
    score = int(input())

    if game_name == 'volleyball':
        volleyball_score += score * 1.07
        volleyball += 1

    elif game_name == 'tennis':
        tennis_score += score * 1.05
        tennis += 1

    elif game_name == 'badminton':
        badminton_score += score * 1.02
        badminton += 1

    try:
        avg_volleyball = volleyball_score / volleyball
    except:
        volleyball = 0

    try:
        avg_tennis = tennis_score / tennis
    except:
        tennis = 0
    try:
        avg_badminton = badminton_score / badminton
    except:
        badminton = 0

    total_score = m.floor(volleyball_score + tennis_score + badminton_score)

if avg_volleyball >= 75\
    and avg_tennis >= 75\
        and avg_badminton >= 75:
    print(f"Congratulations, {player}! You won the cruise games with {total_score} points.")

else:
    print(f"Sorry, {player}, you lost. Your points are only {total_score}.")

 # ************************************************ 06.trip expenses (nested loop) ***********************************************************

vacation = int(input())
left = 0

for day in range(1, vacation + 1):
    price = input()
    budget = 60
    budget = budget + left
    products = 0

    while not price == 'Day over':
        price = int(price)
        budget -= price
        products += 1

        if budget <= 0:
            left = 0
            print(f"Daily limit exceeded! You've bought {products} products.")
            break

        if budget > 0:
            left = budget

        price = input()

    else:
        left = budget
        print(f"Money left from today: {budget:.2f}. You've bought {products} products.")


 # ************************************************ 06.baking competition (nested loop) ******************************************************

participants = int(input())
sold = 0
earned = 0

for participant in range(1, participants + 1):
    name = input()
    bakery = input()

    cookies = 0  # need to be nullified for the next participant
    cakes = 0
    waffles = 0

    while not bakery == 'Stop baking!':
        baked = int(input())

        if bakery == 'cookies':
            cookies += baked
            earned += (baked * 1.50)

        elif bakery == 'cakes':
            cakes += baked
            earned += (baked * 7.80)

        elif bakery == 'waffles':
            waffles += baked
            earned += (baked * 2.30)

        bakery = input()

    print(f"{name} baked {cookies} cookies, {cakes} cakes and {waffles} waffles.")
    sold += (cookies + cakes + waffles)

print(f"All bakery sold: {sold}")
print(f"Total sum for charity: {earned:.2f} lv.")