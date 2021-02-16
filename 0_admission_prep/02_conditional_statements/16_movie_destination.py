

 # ************ 03.movie destination (nested condtiinal statements) ************

budget = float(input())
destination = input()
season = input()
days = int(input())
price = 0

if destination == 'Dubai':
    if season == 'Winter':
        price = 45000
    elif season == 'Summer':
        price = 40000
    price *= 0.70

elif destination == 'Sofia':
    if season == 'Winter':
        price = 17000
    elif season == 'Summer':
        price = 12500
    price *= 1.25

elif destination == 'London':
    if season == 'Winter':
        price = 24000
    elif season == 'Summer':
        price = 20250

total_cost = price * days
left = abs(budget-total_cost)

if total_cost <= budget:
    print(f"The budget for the movie is enough! We have {left:.2f} leva left!")
else:
    print(f"The director needs {left:.2f} leva more!")
