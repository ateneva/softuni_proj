import math as m

# greater number---------------------------------------------
digit = int(input())
number = int(input())

if digit > number:
    print(digit)
else:
    print(number)


# even or odd ------------------------------------------------
digit = int(input())

if digit % 2 > 0:
    print('odd')
else:
    print('even')

# digits in words---------------------------------------------

digit = int(input())

if digit == 1:
    print('one')

elif digit == 2:
    print('two')

elif digit == 3:
    print('three')

elif digit == 4:
    print('four')

elif digit == 5:
    print('five')

elif digit == 6:
    print('six')

elif digit == 7:
    print('seven')

elif digit == 8:
    print('eight')

elif digit == 9:
    print('nine')

else:
    print('number too big')


# numbers between 100 and 200--------------------------------------------
digit = int(input())

if digit < 100:
        print('Less than 100')

elif digit >= 100 and digit <= 200:
        print('Between 100 and 200')

elif digit > 200:
        print('Greater than 200')

# guess the password------------------------------------------------------
given_password = input()
correct_password = 's3cr3t!P@ssw0rd'

if given_password == correct_password:
        print('Welcome')
else:
        print('Wrong password!')

# calculate the area of the given figure----------------------------------
figure = input()

if figure == 'square':
        length = float(input())
        area = length**2
        print('%.3f' % area)

elif figure == 'rectangle':
        length = float(input())
        height = float(input())
        area = length * height
        print('%.3f' % area)

elif figure == 'circle':
        radius = float(input())
        area = radius**2 * m.pi
        print('%.3f' % area)

elif figure == 'triangle':
        length = float(input())
        height = float(input())
        area = length * height / 2
        print('%.3f' % area)


# day of the week -----------------------------------------------------------
day = int(input())

if day == 1:
        print('Monday')
elif day == 2:
        print('Tuesday')
elif day == 3:
        print('Wednesday')
elif day == 4:
        print('Thursday')
elif day == 5:
        print('Friday')
elif day == 6:
        print('Saturday')
elif day == 7:
        print('Sunday')
else:
        print('Error')

# animal type-----------------------------------------------------------------
animal = input()

if animal == 'dog':
        print('mammal')

elif animal == 'snake'\
        or animal == 'tortoise'\
        or animal == 'crocodile':
        print('reptile')
else:
        print('unknown')

# toy shop (exam problem)-------------------------------------------------------

trip_price = float(input())
jigsaws = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

total_price = jigsaws * 2.60 \
              + dolls * 3 \
              + bears * 4.10\
              + minions * 8.2 \
              + trucks * 2
print(total_price)               # 1.calculate total price without discount


units = jigsaws + dolls + bears + minions + trucks
print(units)                     # 2.calculate total units


if units >= 50:
        discount = total_price * 0.25
else:
        discount = 0
print(discount)                  # 3.calculate discount


revenue = total_price - discount
print(revenue)                   # 4.calculate total revenue

money = revenue - revenue*0.10
print(money)                     # 5.calculate money after rent

if money >= trip_price:
        left = money - trip_price
        print('Yes! %.2f lv left.' % left)
else:
        left = abs(money - trip_price)
        print('Not enough money! %.2f lv needed.' % left)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Lab session~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# summing up seconds
player_1 = int(input())
player_2 = int(input())
player_3 = int(input())

total_time = (player_1 + player_2 + player_3)
minutes = m.floor(total_time / 60)
seconds = (player_1 + player_2 + player_3) % 60

if seconds < 10:
    print(f'%d:0%d' % (minutes, seconds))
else:
    print(f'%d:%d' % (minutes, seconds))


# bonus points---------------------------------------------------------------
number = int(input())

if number <= 100:
    if number % 2 == 0:
        bonus_points = 6

    elif number % 5 == 0:
        bonus_points = 7

    else:
        bonus_points = 5
    number += bonus_points

elif number > 100 and number <= 1000:
    if number % 2 == 0:
        bonus_points = number * 0.20 + 1

    elif number % 5 == 0:
        bonus_points = number * 0.20 + 2

    else:
        bonus_points = number * 0.20
    number += bonus_points

elif number > 1000:
    if number % 2 == 0:
        bonus_points = number * 0.10 + 1

    elif number % 5 == 0:
        bonus_points = number * 0.10 + 2

    else:
        bonus_points = number * 0.10
    number += bonus_points

print(bonus_points)
print(number)

# speed info----------------------------------------------------------
speed = float(input())

if speed <= 10:
    print('slow')

elif speed > 10 \
        and speed <= 50:
    print('average')

elif speed > 50 \
        and speed <= 150:
    print('fast')

elif speed > 150 \
        and speed <= 1000:
    print('ultra fast')

else:
    print('extremely fast')


# measurements converter---------------------------------------------------

values = float(input())
measure_from = input()
measure_to = input()

if measure_from == 'mm' \
        and measure_to == 'cm':
    values = values / 10
    print('%.3f' % values)

elif measure_from == 'mm' \
        and measure_to == 'm':
    values = values / 1000
    print('%.3f' % values)

elif measure_from == 'm' \
        and measure_to == 'cm':
    values = values * 100
    print('%.3f' % values)

elif measure_from == 'm' \
        and measure_to == 'mm':
    values = values * 1000
    print('%.3f' % values)

elif measure_from == 'cm' \
        and measure_to == 'm':
    values = values / 100
    print('%.3f' % values)

elif measure_from == 'cm' \
        and measure_to == 'mm':
    values = values * 10
    print('%.3f' % values)


# time + 15 minutes ------------------------------------------------------------
hour = int(input())
minutes = int(input())

if hour < 23 \
        and minutes >= 45:
    hour += 1
    minutes = (minutes + 15) % 60

elif hour >= 23 \
        and minutes >= 45:
        hour = 0
        minutes = (minutes + 15) % 60
else:
    minutes = minutes + 15

if minutes < 10:
    print(f'%d:0%d' % (hour, minutes))
else:
    print(f'%d:%d' % (hour, minutes))

# godzilla vs. kong (exam problem)----------------------------------------------
budget = float(input())
cast = int(input())
costume = float(input())

decor = budget * 0.10
print(decor)

if cast >= 150:
    costume = (costume * cast) - (costume * cast * 0.10)
    print(costume)

else:
    costume = costume * cast
    print(costume)

expenses = decor + costume
print(expenses)

if expenses > budget:
    left = abs(budget-expenses)
    print('Not enough money!')
    print('Wingard needs %.2f leva more.' % left)

elif expenses <= budget:
    left = abs(budget-expenses)
    print('Action!')
    print('Wingard starts filming with %.2f leva left.' % left)

# swimming record (exam problem)------------------------------------------------
world_record = float(input())  # seconds
distance = float(input())      # metres
speed_per_m = float(input())   # seconds

time_to_swim = distance * speed_per_m
print(time_to_swim)

additional_time = m.floor(distance / 15) * 12.5
print(additional_time)

total_time = time_to_swim + additional_time
print(total_time)

if total_time < world_record:
    new_record = total_time
    print(new_record)
    print('Yes, he succeeded! The new world record is %.2f seconds.' % new_record)

else:
    new_record = abs(world_record-total_time)
    print(new_record)
    print('No, he failed! He was %.2f seconds slower.' % new_record)


# scholarships (exam problem)---------------------------------------------------
income = float(input())
grades = float(input())
minimum_wage = float(input())

if grades >= 5.5 \
        and income >= minimum_wage:
    excellent_scholarship = m.floor(grades * 25)
    print(excellent_scholarship)
    print('You get a scholarship for excellent results %.0f BGN' % excellent_scholarship)

elif grades > 4.5 \
        and income < minimum_wage:
    social_scholarship = m.floor(minimum_wage * 0.35)
    excellent_scholarship = m.floor(grades * 25)
    print(social_scholarship)
    print(excellent_scholarship)

    if excellent_scholarship >= social_scholarship:
        print('You get a scholarship for excellent results %.0f BGN' % excellent_scholarship)
    else:
        print('You get a Social scholarship %.0f BGN' % social_scholarship)

else:
    print('You cannot get a scholarship!')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ More exercies ~~~~~~~~~~~~~~~~~~~~~~~~~~~
weather = float(input())

if weather >= 26\
        and weather <= 35:
    print("Hot")

elif weather >= 20.1\
        and weather <= 25.9:
    print("Warm")

elif weather >= 15.00\
        and weather <= 20.00:
    print("Mild")

elif weather >= 12.00\
        and weather <= 14.9:
    print("Cool")

elif weather >= 5.00\
        and weather <= 11.9:
    print("Cold")

else:
    print("unknown")
