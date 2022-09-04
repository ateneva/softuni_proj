
# **************01.food delivery (simple calculations) *************************

chicken_menus = int(input())
fish_menus = int(input())
veggie_menus = int(input())

chicken = chicken_menus * 10.35
fish = fish_menus * 12.40
veggie = veggie_menus * 8.15

dessert = (chicken + fish + veggie) * 0.20
total = chicken + fish + veggie + dessert + 2.50

print(f"Total: {total:.2f}")

# ************ 02.safari (conditional statements) ******************************

budget = float(input())
petrol_needed = float(input())
day = input()

petrol = petrol_needed * 2.10
total = petrol + 100

if day == 'Saturday':
    total *= 0.90
else:
    total *= 0.80

left = abs(budget-total)

if total <= budget:
    print(f"Safari time! Money left: {left:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {left:.2f} lv.")

# *************03.mobile operator (nested condtiinal statements) ***************

contract_length = input()
contract_type = input()
data_plan = input()
months = int(input())
monthly_fee = 0

if contract_length == 'one':
    if contract_type == 'Small':
        monthly_fee = 9.98

    elif contract_type == 'Middle':
        monthly_fee = 18.99

    elif contract_type == 'Large':
        monthly_fee = 25.98

    elif contract_type == 'ExtraLarge':
        monthly_fee = 35.99

elif contract_length == 'two':
    if contract_type == 'Small':
        monthly_fee = 8.58

    elif contract_type == 'Middle':
        monthly_fee = 17.09

    elif contract_type == 'Large':
        monthly_fee = 23.59

    elif contract_type == 'ExtraLarge':
        monthly_fee = 31.79


if data_plan == 'yes':
    if monthly_fee <= 10.00:
        monthly_fee += 5.50

    elif monthly_fee > 10 and monthly_fee <= 30:
        monthly_fee += 4.35

    elif monthly_fee > 30:
        monthly_fee += 3.85

total = months * monthly_fee

if contract_length == 'two':
    total -= (total * 3.75/100)

print(f"{total:.2f} lv.")

# *****************04.while loop (while loop) **********************************

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

# **********05.division without remainder (for loop) ***************************

n = int(input())
p1 = 0
p2 = 0
p3 = 0

for i in range(n):
    num = int(input())

    if num % 2 == 0:
        p1 += 1

    if num % 3 == 0:
        p2 += 1

    if num % 4 == 0:
        p3 += 1

print(f'{p1 / n * 100 :.2f}%')
print(f'{p2 / n * 100 :.2f}%')
print(f'{p3 / n * 100 :.2f}%')


# ***********06.vet parking (nested loop) **************************************

days = int(input())
hours = int(input())
fee = 0
total_fees = 0

for d in range(1, days + 1):
    day_total = 0

    for h in range(1, hours + 1):
        if d % 2 == 0 and h % 2 != 0:
            fee = 2.50
        elif d % 2 != 0 and h % 2 == 0:
            fee = 1.25
        else:
            fee = 1.00

        day_total += fee

    print(f"Day: {d} - {day_total:.2f} leva")

    total_fees += day_total

print(f"Total: {total_fees:.2f} leva")
