
# ******** 03.world snooker championship (nested condtiinal statements) ********

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
