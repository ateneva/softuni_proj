
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
