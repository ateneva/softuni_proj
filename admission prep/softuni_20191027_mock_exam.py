
# sea trip (simple calculations) *********************************************************

food_per_day = float(input())
gifts_per_day = float(input())
hotel_per_day = float(input())

distance = 210 * 2
days = 3
petrol_price = 1.85
petrol_needed = distance / 100 * 7

petrol_money = petrol_needed * petrol_price
#print(petrol_money)

hotel_expenses = hotel_per_day * 0.90 \
                 + hotel_per_day * 0.85 \
                 + hotel_per_day * 0.80

#print(hotel_expenses)

total_needed = food_per_day * days \
               + gifts_per_day * days \
               + hotel_expenses \
               + petrol_money

print(f'Money needed: {total_needed:.2f}')

# spaceship (conditional statements)*****************************************************
import math as m

spaceship_width = float(input())
spaceship_length = float(input())
spaceship_height = float(input())
avg_height = float(input())

l = 2
w = 2
h = 0.40 + avg_height

spaceship_volume = spaceship_width * spaceship_length * spaceship_height
room_volume = l * w * h
participants = m.floor(spaceship_volume/room_volume)

# print(spaceship_volume)
# print(room_volume)
# print(participants)

if participants < 3:
    print("The spacecraft is too small.")

elif participants >= 3 and participants < 10:
    print(f'The spacecraft holds {participants} astronauts.')

elif participants >= 10:
    print('The spacecraft is too big.')

# sushi time (nested conditional statements)***************************************
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

# bachelor party (while loops)*******************************************************************
guest_fee = int(input())
people = input()
meal_price = 0
total_meal_price = 0
total_people = 0

while not people == 'The restaurant is full':
        people = int(people)
        if people < 5:
            meal_price += people * 100

        elif people >= 5:
            meal_price += people * 70

        total_people += people
        total_meal_price = meal_price

        people = input()

        #print(meal_price)
        #print(total_meal_price)

left = abs(total_meal_price - guest_fee)
if total_meal_price >= guest_fee:
    print(f'You have {total_people} guests and {left} leva left.')
else:
    print(f'You have {total_people} guests and {total_meal_price} leva income, but no singer.')

# bus stops *************************************************************************************

starting_passengers = int(input())
stops = int(input())

for i in range(1, stops + 1):
    off = int(input())
    on = int(input())

    starting_passengers += on
    starting_passengers -= off

    if i % 2 != 0:
        starting_passengers += 2
    else:
        starting_passengers -= 2

    #print(starting_passengers)
print(f'The final number of passengers is : {starting_passengers}')


# multiplication table ****************************************************************************
number = int(input())

start = int(str(number)[-1:])
mid = int(str(number)[-2])
end = int(str(number)[:1])

for i in range(1, start+1):
    for j in range(1, mid+1):
        for k in range(1, end+1):
            print(f'{i} * {j} * {k} = {i * j * k};')