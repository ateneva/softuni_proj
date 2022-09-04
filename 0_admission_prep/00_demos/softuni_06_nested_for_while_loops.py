
# **************06.trip expenses (nested loop) *********************************
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


 # ************06.baking competition (nested loop) *****************************
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


# *********06.Easter Competition (nested loop) *********************************

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


# ************06.Easter Decoration (nested loop) *******************************

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
