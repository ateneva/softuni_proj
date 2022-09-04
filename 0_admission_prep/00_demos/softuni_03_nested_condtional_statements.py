
# personal titles--------------------------------------
age = float(input())
gender = input()

if gender == 'm' and age >= 16:
    print('Mr.')

elif gender == 'm' and age < 16:
    print("Master")

elif gender == 'f' and age >= 16:
    print('Ms.')

elif gender == 'f' and age < 16:
    print('Miss')

# small shop--------------------------------------------
product = input()
city = input()
volume = float(input())

if city == 'Sofia':
    if product == 'coffee':
        price = volume * 0.5
        print(price)
    if product == 'water':
        price = volume * 0.8
        print(price)
    if product == 'beer':
        price = volume * 1.20
        print(price)
    if product == 'sweets':
        price = volume * 1.45
        print(price)
    if product == 'peanuts':
        price = volume * 1.60
        print(price)

elif city == 'Plovdiv':
    if product == 'coffee':
        price = volume * 0.4
        print(price)
    if product == 'water':
        price = volume * 0.7
        print(price)
    if product == 'beer':
        price = volume * 1.15
        print(price)
    if product == 'sweets':
        price = volume * 1.30
        print(price)
    if product == 'peanuts':
        price = volume * 1.50
        print(price)

elif city == 'Varna':
    if product == 'coffee':
        price = volume * 0.45
        print(price)
    if product == 'water':
        price = volume * 0.7
        print(price)
    if product == 'beer':
        price = volume * 1.10
        print(price)
    if product == 'sweets':
        price = volume * 1.35
        print(price)
    if product == 'peanuts':
        price = volume * 1.55
        print(price)

# number in range ---------------------------------------
number = int(input())

if number != 0:
    if number >= -100 and number <= 100:
        print('Yes')
    else:
        print('No')
else:
    print('No')

# fruit or vegetable---------------------------------------
product = input()

if product == 'banana' \
    or product == 'apple' \
    or product == 'kiwi' \
    or product == 'cherry' \
    or product == 'lemon' \
    or product == 'grapes':
        print('fruit')

elif product == 'tomato' \
        or product == 'cucumber' \
        or product == 'pepper' \
        or product == 'carrot':
        print('vegetable')

else:
    print('unknown')

# invalid number -------------------------------
number = int(input())

if number >= 100 and number <= 200 \
    or number == 0:
    print('')

else:
    print('invalid')

# fruit shop -----------------------------------
fruit = input()
day = input()
amount = float(input())

if day == 'Monday' \
    or day == 'Tuesday' \
    or day == 'Wednesday' \
    or day == 'Thursday' \
    or day == 'Friday':
        if fruit == 'banana':
            price = 2.50
        elif fruit =='apple':
            price = 1.20
        elif fruit == 'orange':
            price = 0.85
        elif fruit == 'grapefruit':
            price = 1.45
        elif fruit == 'kiwi':
            price = 2.70
        elif fruit == 'pineapple':
            price = 5.50
        elif fruit == 'grapes':
            price = 3.85

        try:
            payable = price * amount
            print('%.2f' % payable)
        except:
            print('error')

elif day == 'Saturday' \
        or day == 'Sunday':
            if fruit == 'banana':
                price = 2.70
            elif fruit == 'apple':
                price = 1.25
            elif fruit == 'orange':
                price = 0.90
            elif fruit == 'grapefruit':
                price = 1.60
            elif fruit == 'kiwi':
                price = 3.00
            elif fruit == 'pineapple':
                price = 5.60
            elif fruit == 'grapes':
                price = 4.20

            try:
                payable = price * amount
                print('%.2f' % payable)
            except:
                print('error')

else:
    print('error')

# trade commissions---------------------------------------------
city = input()
sales = float(input())

if city == 'Sofia' and sales > 0:
        if sales >= 0 and sales <= 500:
            commission = 0.05
        elif sales > 500 and sales <= 1000:
            commission = 0.07
        elif sales > 1000 and sales <= 10000:
            commission = 0.08
        elif sales > 10000:
            commission = 0.12
        try:
            payable = sales * commission
            print('%.2f' % payable)
        except:
            print('error')

elif city == 'Varna' and sales > 0:
        if sales >= 0 and sales <= 500:
            commission = 0.045
        elif sales > 500 and sales <= 1000:
            commission = 0.075
        elif sales > 1000 and sales <= 10000:
            commission = 0.10
        elif sales > 10000:
            commission = 0.13
        try:
            payable = sales * commission
            print('%.2f' % payable)
        except:
            print('error')

elif city == 'Plovdiv' and sales > 0:
        if sales >= 0 and sales <= 500:
            commission = 0.055
        elif sales > 500 and sales <= 1000:
            commission = 0.08
        elif sales > 1000 and sales <= 10000:
            commission = 0.12
        elif sales > 10000:
            commission = 0.145
        try:
            payable = sales * commission
            print('%.2f' % payable)
        except:
            print('error')

else:
    print('error')

# ski trip -------------------------------------------------------
days = int(input())
accommodation = input()
review = input()

if accommodation == 'room for one person':
    discount = 0
    price = (days-1) * 18
    if review == 'positive':
        price += price * 0.25
    elif review == 'negative':
        price -= price * 0.10
    print('%.2f' % price)

elif accommodation == 'apartment':
    price_per_night = 25
    if days < 10:
        discount = 0.30
        price = (days-1) * price_per_night * (1-discount)

        if review == 'positive':
            price += price * 0.25
        elif review == 'negative':
            price -= price * 0.10
        print('%.2f' % price)

    elif days >= 10 and days <= 15:
        discount = 0.35
        price = (days-1) * price_per_night * (1-discount)

        if review == 'positive':
            price += price * 0.25
        elif review == 'negative':
            price -= price * 0.10
        print('%.2f' % price)

    elif days > 15:
        discount = 0.50
        price = (days-1) * price_per_night * (1 - discount)

        if review == 'positive':
            price += price * 0.25
        elif review == 'negative':
            price -= price * 0.10
        print('%.2f' % price)

elif accommodation == 'president apartment':
    price_per_night = 35
    if days < 10:
        discount = 0.10
        price = (days-1) * price_per_night * (1 - discount)

        if review == 'positive':
            price += price * 0.25
        elif review == 'negative':
            price -= price * 0.10
        print('%.2f' % price)

    elif days >= 10 and days <= 15:
        discount = 0.15
        price = (days-1) * price_per_night * (1 - discount)

        if review == 'positive':
            price += price * 0.25
        elif review == 'negative':
            price -= price * 0.10
        print('%.2f' % price)

    elif days > 15:
        discount = 0.20
        price = (days-1) * price_per_night * (1 - discount)

        if review == 'positive':
            price += price * 0.25
        elif review == 'negative':
            price -= price * 0.10
        print('%.2f' % price)

#------------------------------------ Exercies----------------------------------
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

first_condition = (x == x1 or x == x2) and (y1 <= y <= y2)
second_condition = (y ==y1 or y == y2) and (x1 <= x <= x2)

if first_condition == True or second_condition == True:
    print('Border')
else:
    print('Inside / Outside')


# cinema-------------------------------------------------------------------
screening = input()
rows = int(input())
columns = int(input())

if screening == 'Premiere':
    price = 12
    revenue = rows * columns * price
    print('%.2f leva' % revenue)

elif screening == 'Normal':
    price = 7.5
    revenue = rows * columns * price
    print('%.2f leva' % revenue)

elif screening == 'Discount':
    price = 5
    revenue = rows * columns * price
    print('%.2f leva' % revenue)

# summer outfit----------------------------------------------------------
degrees = int(input())
timeofday = input()

if degrees >=10 and degrees <= 18:
    if timeofday == 'Morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'

    elif timeofday == 'Afternoon':
        outfit = 'Shirt'
        shoes = 'Moccasins'

    elif timeofday == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

elif degrees > 18 and degrees <= 24:
    if timeofday == 'Morning':
        outfit = 'Shirt'
        shoes = 'Moccasins'

    elif timeofday == 'Afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'

    elif timeofday == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

elif degrees >= 25:
    if timeofday == 'Morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'

    elif timeofday == 'Afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'

    elif timeofday == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

# new house---------------------------------------------------------------------
flower = input()
volume = int(input())
budget = int(input())

if flower == 'Roses':
    base_price = 5
    if volume > 80:
        discount = 0.10
        price = base_price * (1-discount)
    else:
        discount = 0
        price = base_price
    final_price = volume * price

elif flower == 'Dahlias':
    base_price = 3.80
    if volume > 90:
        discount = 0.15
        price = base_price * (1-discount)
    else:
        discount = 0
        price = base_price
    final_price = volume * price

elif flower == 'Tulips':
    base_price = 2.80
    if volume > 80:
        discount = 0.15
        price = base_price * (1-discount)
    else:
        discount = 0
        price = base_price
    final_price = volume * price

elif flower == 'Narcissus':
    base_price = 3
    if volume < 120:
        discount = 0.15
        price = base_price * (1+discount)
    else:
        discount = 0
        price = base_price
    final_price = volume * price

elif flower == 'Gladiolus':
    base_price = 2.5
    if volume < 80:
        discount = 0.20
        price = base_price * (1+discount)
    else:
        discount = 0
        price = base_price
    final_price = volume * price

remaining = budget - final_price
needed = abs(remaining)

if remaining >= 0:
    print(f"Hey, you have a great garden with {volume} {flower} and %.2f leva left." % remaining)

elif remaining < 0:
    print(f"Not enough money, you need %.2f leva more." % needed)

# fishing boat------------------------------------------------------------------
budget = int(input())
season = input()
fishermen = int(input())

if season == 'Spring':
    base_price = 3000
    if fishermen <= 6:
        base_discount = 0.10
    elif fishermen >= 7 and fishermen <=11:
        base_discount = 0.15
    elif fishermen >= 12:
        base_discount = 0.25

    first_discounted = base_price * (1-base_discount)
    if fishermen % 2 == 0:
        price = first_discounted * 0.95
    else:
        price = first_discounted

elif season == 'Summer' or season == 'Autumn':
    base_price = 4200
    if fishermen <= 6:
        base_discount = 0.10
    elif fishermen >= 7 and fishermen <= 11:
        base_discount = 0.15
    elif fishermen >= 12:
        base_discount = 0.25

    first_discounted = base_price * (1 - base_discount)
    if fishermen % 2 == 0 and season != 'Autumn':
        price = first_discounted * 0.95
    else:
        price = first_discounted

elif season == 'Winter':
    base_price = 2600
    if fishermen <= 6:
        base_discount = 0.10
    elif fishermen >= 7 and fishermen <= 11:
        base_discount = 0.15
    elif fishermen >= 12:
        base_discount = 0.25

    first_discounted = base_price * (1 - base_discount)
    if fishermen % 2 == 0:
        price = first_discounted * 0.95
    else:
        price = first_discounted

remaining = abs(budget-price)

if budget >= price:
    print(f"Yes! You have %.2f leva left." % remaining)
elif budget < price:
    print(f"Not enough money! You need %.2f leva." % remaining)

# journey ----------------------------------------------------------------------
budget = float(input())
season = input()

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        stay = 'Camp'
        expenses = budget * 0.3

    elif season == 'winter':
        stay = 'Hotel'
        expenses = budget * 0.7

elif budget > 100 and budget <=1000:
    destination = 'Balkans'
    if season == 'summer':
        stay = 'Camp'
        expenses = budget * 0.4

    elif season == 'winter':
        stay = 'Hotel'
        expenses = budget * 0.8

elif budget > 1000:
    destination = 'Europe'
    stay = 'Hotel'
    expenses = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{stay} - %.2f" % expenses)

# operations between numbers----------------------------------------------------
n1 = int(input())
n2 = int(input())
operator = input()

if operator == '+':
    result = n1 + n2
    if result % 2 == 0:
        digit = 'even'
    else:
        digit = 'odd'
    print(f"{n1} {operator} {n2} = {result} - {digit}")

elif operator == '-':
    result = n1 - n2
    if result % 2 == 0:
        digit = 'even'
    else:
        digit = 'odd'
    print(f"{n1} {operator} {n2} = {result} - {digit}")

elif operator == '*':
    result = n1 * n2
    if result % 2 == 0:
        digit = 'even'
    else:
        digit = 'odd'
    print(f"{n1} {operator} {n2} = {result} - {digit}")

elif operator == '/':
    if n2 > 0 or n2 < 0:
        result = n1/n2
        print(f"{n1} {operator} {n2} = %.2f" % result)
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")

elif operator == '%':
    if n2 > 0 or n2 < 0:
        result = n1 % n2
        print(f"{n1} {operator} {n2} = {result}")
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")

# hotel room -------------------------------------------------------------------
month = input()
nights = int(input())

if month == 'May' or month == 'October':
     if nights > 7 and nights < 14:
         discount = 0.05
         studio = nights * 50 * (1-discount)
         apartment = nights * 65

     elif nights > 14:
         discount = 0.30
         studio = nights * 50 * (1-discount)
         apartment = nights * 65 * 0.90

     else:
         studio = nights * 50
         apartment = nights * 65

elif month == 'June' or month == 'September':
    if nights > 14:
        discount = 0.20
        studio = nights * 75.20 * (1 - discount)
        apartment = nights * 68.70 * 0.90
    else:
        studio = nights * 75.20
        apartment = nights * 68.70

elif month == 'July' or month == 'August':
    if nights > 14:
        studio = nights * 76
        apartment = nights * 77 * 0.90
    else:
        studio = nights * 76
        apartment = nights * 77

print(f"Apartment: %.2f lv." % apartment)
print(f"Studio: %.2f lv." % studio)

# on time for exam--------------------------------------------------------------
exam_hour = int(input()) * 60
exam_minute = int(input())
arrival_hour = int(input()) * 60
arrival_minute = int(input())

arrival_time = arrival_hour + arrival_minute
exam_time = exam_hour + exam_minute

minutes_diff = arrival_time - exam_time
hours_diff = abs(minutes_diff) // 60
min_diff = abs(minutes_diff) % 60

if minutes_diff < -30:
    print('Early')
    if hours_diff > 0:
        print(f"{hours_diff}:{min_diff:02} hours before the start")
    else:
        print(f"{min_diff:02} minutes before the start")

elif minutes_diff <= 0:
    print('On time')
    if min_diff > 0:
        print(f"{min_diff} minutes before the start")
    else:
        print('')

elif minutes_diff > 0:
    print('Late')
    if hours_diff > 0:
        print(f"{hours_diff}:{min_diff:02} hours after the start")
    else:
        print(f"{min_diff:02} minutes after the start")

# volleyball--------------------------------------------------------------------
import math as m

year = input()
weekends = 48
praznici = int(input())
hometown = int(input())

if year == 'normal':
    volleyball = praznici * (2/3) \
        + (weekends-hometown) * (3/4) \
        + hometown
    print(m.floor(volleyball))

else:
    volleyball = praznici * (2/3) \
        + (weekends-hometown) * (3/4) \
        + hometown

    volleyball += volleyball * 0.15
    print(m.floor(volleyball))


# Mock Exam 2019-10-27 sushi time (nested conditional statements)***************
import math as m

sushi_type = input()
place = input()
quantity = int(input())
order = input()

if place == 'Sushi Zone':
    if sushi_type == 'sashimi':
        price = 4.99
    elif sushi_type == 'maki':
        price = 5.29
    elif sushi_type == 'uramaki':
        price = 5.99
    elif sushi_type == 'temaki':
        price = 4.29

    if order == 'N':
        meal_price = m.ceil(price * quantity)
    else:
        meal_price = m.ceil(price * quantity * 1.20)
    print(f'Total price: {meal_price} lv.')

elif place == 'Sushi Time':
    if sushi_type == 'sashimi':
        price = 5.49
    elif sushi_type == 'maki':
        price = 4.69
    elif sushi_type == 'uramaki':
        price = 4.49
    elif sushi_type == 'temaki':
        price = 5.19

    if order == 'N':
        meal_price = m.ceil(price * quantity)
    else:
        meal_price = m.ceil(price * quantity * 1.20)
    print(f'Total price: {meal_price} lv.')

elif place == 'Sushi Bar':
    if sushi_type == 'sashimi':
        price = 5.25
    elif sushi_type == 'maki':
        price = 5.55
    elif sushi_type == 'uramaki':
        price = 6.25
    elif sushi_type == 'temaki':
        price = 4.75

    if order == 'N':
        meal_price = m.ceil(price * quantity)
    else:
        meal_price = m.ceil(price * quantity * 1.20)
    print(f'Total price: {meal_price} lv.')

elif place == 'Asian Pub':
    if sushi_type == 'sashimi':
        price = 4.50
    elif sushi_type == 'maki':
        price = 4.80
    elif sushi_type == 'uramaki':
        price = 5.50
    elif sushi_type == 'temaki':
        price = 5.50

    if order == 'N':
        meal_price = m.ceil(price * quantity)
    else:
        meal_price = m.ceil(price * quantity * 1.20)
    print(f'Total price: {meal_price} lv.')

else:
    print(f'{place} is invalid restaurant!')


# Admission exm 2019-11-03 game statistics *************************************

minutes = int(input())
player = input()

if minutes == 0:
    print(f'Match has just began!')

elif minutes > 0 and minutes < 45:
    print(f'First half time.')

    if minutes >= 1 and minutes <= 10:
        print(f'{player} missed a penalty.')
        if minutes % 2 == 0:
            print(f'{player} was injured after the penalty.')

    elif minutes > 10 and minutes <= 35:
        print(f'{player} received yellow card.')
        if minutes % 2 != 0:
            print(f'{player} got another yellow card.')

    elif minutes > 35 and minutes < 45:
        print(f'{player} SCORED A GOAL !!!')

elif minutes >= 45:
    print(f'Second half time.')

    if minutes > 45 and minutes <= 55:
        print(f'{player} got a freekick.')
        if minutes % 2 == 0:
            print(f'{player} missed the freekick.')

    elif minutes > 55 and minutes <= 80:
        print(f'{player} missed a shot from corner.')
        if minutes % 2 != 0:
            print(f'{player} has been changed with another player.')

    elif minutes > 80 and minutes <= 90:
        print(f'{player} SCORED A GOAL FROM PENALTY !!!')
