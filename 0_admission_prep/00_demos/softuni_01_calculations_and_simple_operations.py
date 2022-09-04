import math as m

# greeting by name
first_name = input()
last_name = input()
age = int(input())
town = input()

#----------format a string and take variables into account----------------------

# 'You are {first_name} {last_Name}, -years old person from {town}
print('You are ' + first_name + ' ' + last_name + ', a ' + str(age) + '-years old person from ' + town)
print(f'You are {first_name} {last_name}, a {age}-years old person from {town}.')
print('You are %s %s, a %d-years old person from %s.' % (first_name, last_name, age, town))
# %s --> string
# %d --> digit

# inches to centimeters
inches = float(input())
centimeters = inches * 2.54
print(centimeters)
print(round(centimeters, 3))     # round uses standard math logic <5 rounds down, >5 rounds up
print(f'{centimeters:.4f}')      # unlike round approach, this one adds padding 0s (test with input 10)
print('%.2f' % centimeters)

# projects creation------------------------------------------------------
architect = input()
projects = int(input())
hours = projects * 3
print(f'The architect %s will need %d hours to complete %d project/s.'
      % (architect, hours, projects))

# circle area and perimeter----------------------------------------------
r = float(input())
area = m.pi * r * r
perimeter = r * m.pi * 2
print('%.2f' % area)
print('%.2f' % perimeter)

# pet shop---------------------------------------------------------------
dogs = int(input())
animals = int(input())
amount = (dogs * 2.50) + animals * 4
print('%.2f lv.' % amount)

# yard greening----------------------------------------------------------
sqm = float(input())
price = 7.61
discount = 0.18

paid = sqm * price * (1-discount)
discount_given = abs(paid - (sqm * price))
print('The final price is: %.2f lv.' % paid)
print('The discount is: %.2f lv.' % discount_given)


# aquarium (exam problem)-------------------------------------------------------
length = int(input())
width = int(input())
height = int(input())
percent_other = float(input())

volume = length * width * height / 1000
taken = percent_other * 0.01
water = volume - volume * taken
print('%.3f' % water)

# -------------------------------------------lab session------------------------
# exchange rate
USD = float(input())
rate = 1.79549
BGN = USD * rate
print('%.2f' % BGN)

# radians to degrees------------------------------------------------------------
radians = float(input())
degrees = radians * 180 / m.pi
print(round(degrees))
print('%.1f' % degrees)

# rectangle area----------------------------------------------------------------
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

length = abs(x1-x2)
width = abs(y1-y2)
area = length * width
perimeter = 2*length + 2*width

print(f'{area:.2f}')
print(f'{perimeter:.2f}')

# sewing orders a.k.a tailoring workshop (exam problem)-------------------------
tables = int(input())
table_length = float(input())
table_width = float(input())

pokrivka = tables * (table_length + 2*0.30) * (table_width + 2*0.30)
pokrivka_price = pokrivka * 7

kare = tables * (table_length/2) * (table_length/2)
kare_price = kare * 9

dollar_price = pokrivka_price + kare_price
BGN_price = dollar_price * 1.85
print('%.2f USD' % dollar_price)
print('%.2f BGN' % BGN_price)

# dance hall (exam problem)-----------------------------------------------------
length = float(input()) * 100
width = float(input()) * 100
A = float(input()) * 100

area = length * width
bench = area/10
wardrobe = A * A

free_space = area - bench - wardrobe
dancers = m.floor(free_space/(40+7000))
print(dancers)

# charity campaign (exam problem)-----------------------------------------------
days = int(input())
bakers = int(input())

cakes = int(input()) * 45
waffles = int(input()) * 5.80
pancakes = int(input()) * 3.20

revenue_per_baker = (cakes + waffles + pancakes) * bakers
revenue = revenue_per_baker * days

expenses = revenue * 0.125
total = revenue - expenses
print('%.2f' % total)

# alcohol market (exam problem)-------------------------------------------------
price_whisky = float(input())
beer = float(input())
wine = float(input())
rakia = float(input())
whisky = float(input())

price_rakia = price_whisky / 2
price_wine = price_rakia - price_rakia * 0.40
price_beer = price_rakia - price_rakia * 0.80

bill = (whisky * price_whisky) \
        + (beer * price_beer) \
        + (wine * price_wine) \
        + (rakia * price_rakia)

print('%.2f' % bill)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~More exerciese~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# trapezoid area
side_1 = float(input())
side_2 = float(input())
height = float(input())

area = (side_1 + side_2) * height / 2
print('%.2f' % area)

# triangle area --------------------------------------------
side = float(input())
height = float(input())

area = side * height / 2
print('%.2f' % area)

# celsius to fahrenheit--------------------------------------
celsius = float(input())

fahrenheit = (celsius * 9/5) + 32
print('%.2f' % fahrenheit)

# vegetable market-------------------------------------------
vegetable_price_per_kg = float(input())
fruit_price_per_kg = float(input())
vegetables_kg = int(input())
fruit_kg = int(input())

revenue_BGN = (vegetable_price_per_kg * vegetables_kg) \
                + (fruit_price_per_kg * fruit_kg)

revenue_EUR = revenue_BGN/1.94
print('%.2f' % revenue_EUR)
