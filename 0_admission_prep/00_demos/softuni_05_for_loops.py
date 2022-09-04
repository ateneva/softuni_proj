
# numbers from 1 to 100---------------------------------
for i in range(1, 101):
    print(i)

# letters from a to z-----------------------------------
start = ord('a')
end = ord('{')

for i in range(start, end):
    print(chr(i))

# characters sequence-----------------------------------
text = input()

for char in text:
    print(char)

# characters sequence 2---------------------------------
text = input()

for index, char in enumerate(text):
    print(index, char)

# vowels sum----------------------------------------------
text = input()
vowels = 0

for char in text:
    if char == 'a':
        vowels += 1
    elif char == 'e':
        vowels += 2

    elif char == 'i':
        vowels += 3

    elif char == 'o':
        vowels += 4

    elif char == 'u':
        vowels += 5

print(vowels)

# sum numbers--------------------------------------------
numbers = int(input())
sum = 0

for i in range(1, numbers+1):
    i = int(input())
    sum += i

print(sum)

# number sequence----------------------------------------
import sys

numbers = int(input())
max_number = -sys.maxsize
min_number = sys.maxsize
max_count = 0
min_count = 0

for i in range(0, numbers):
    i = int(input())
    max_count += 1
    min_count += 1

    if i > max_number:
        max_number = i

    if i < min_number:
        min_number = i

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')

# left and right sum--------------------------------------------------
numbers = int(input())
i_count = 0
left_sum = 0
right_sum = 0

for i in range(0, 2*numbers):
    i = int(input())
    i_count += 1

    if i_count <= 2*numbers/2:
        left_sum += i

    elif i_count > 2*numbers/2:
        right_sum += i

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {abs(left_sum-right_sum)}')

# odd / even sum -------------------------------------------------------
numbers = int(input())
i_count = 0
odd_sum = 0
even_sum = 0

for index in range(0, numbers):
    i = int(input())
    if index % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

if even_sum == odd_sum:
    print(f'Yes\nSum = {even_sum}')
else:
    print(f'No\nDiff = {abs(even_sum-odd_sum)}')

# numers n to 1 in reversed order---------------------------------------
number = int(input())

for index in reversed(list(range(0, number))):
    i = index + 1
    print(i)

# numbers 1 to n step 3--------------------------------------------------
number = int(input())

for index in range(0, number, 3):  # for each number in range, step 3
    i = index + 1
    print(i)

# even powers of 2-------------------------------------------------------
n = int(input())
num = 1

for i in range(0, n+1, 2):
    num = 2 ** i
    print(num)

# clever Lilly (exam problem)--------------------------------------------
age = int(input())
price_washing_machine = float(input())
toy_price = int(input())
toys = 0
gift_money = 0
gift_sum = 0
given_to_bro = 0

for i in range(1, age+1):
    if i % 2 == 0:
        gift_sum += 10
        gift_money += gift_sum
        given_to_bro += 1

    elif i % 2 != 0:
        toys += 1

sales_income = toys * toy_price
total_money = sales_income + gift_money - given_to_bro

left = abs(total_money - price_washing_machine)
if total_money > price_washing_machine:
    print(f'Yes! %.2f' % left)
else:
    print(f'No! %.2f' % left)

# ------------------------------------Exercises---------------------------------

# numbers ending in 7-----------------------------------
for i in range(1, 1001):
    if i % 10 == 7:
        print(i)

# numbers divided by 3 without remainder----------------

for i in range(1, 100):
    if i % 3 == 0:
        print(i)

# average number-----------------------------------------

n = int(input())
total = 0

for i in range(n):
    i = int(input())
    total += i

print(f'{total/n:.2f}')

# half sum element--------------------------------------
import sys

n = int(input())
i_sum = 0
max_count = 0
max_num = -sys.maxsize

for i in range(0, n):
    i = int(input())
    i_sum += i
    max_count += 1

    if i > max_num:
        max_num = i

i_sum -= max_num
if i_sum == max_num:
    print(f'Yes \nSum = {i_sum}')

else:
    diff = abs(max_num - i_sum)
    print(f'No \nDiff = {diff}')

# odd/even position-------------------------------------------------------------
import sys

n = int(input())
odd_sum = 0
odd_max = -sys.maxsize
odd_min = sys.maxsize

even_sum = 0
even_max = -sys.maxsize
even_min = sys.maxsize

for index in range(1, n+1):
    i = float(input())

    if index % 2 == 0:
        even_sum += i

        if i > even_max:
            even_max = i

        if i < even_min:
            even_min = i

    else:
        odd_sum += i

        if i > odd_max:
            odd_max = i

        if i < odd_min:
            odd_min = i

print(f'OddSum=%.2f,' % odd_sum)

if odd_min == sys.maxsize:
    print('OddMin=No,')
else:
    print(f'OddMin=%.2f,' % odd_min)

if odd_max == -sys.maxsize:
    print('OddMax=No,')
else:
    print(f'OddMax=%.2f,' % odd_max)

print(f'EvenSum=%.2f,' % even_sum)

if even_min == sys.maxsize:
    print('EvenMin=No,')
else:
    print(f'EvenMin=%.2f,' % even_min)

if even_max == -sys.maxsize:
    print('EvenMax=No')
else:
    print(f'EvenMax=%.2f' % even_max)

# equal pairs-------------------------------------------------------------------
numbers = int(input())
i_count = 0
sum = 0
max_diff = 0

for i in range(numbers):
    num1 = int(input())
    num2 = int(input())

    current_sum = num1 + num2
    if i == 0:
        sum = current_sum

    if not current_sum == sum:
        current_diff = abs(sum - current_sum)
        if current_diff > max_diff:
            max_diff = current_diff
        sum = current_sum

if max_diff == 0:
    print(f'Yes, value={sum}')
else:
    print(f'No, maxdiff={max_diff}')

# histogram---------------------------------------------------------------------
n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(n):
    num = int(input())

    if num < 200:
        p1 += 1

    elif num >= 200 and num <= 399:
        p2 += 1

    elif num >= 400 and num <= 599:
        p3 += 1

    elif num >= 600 and num <= 799:
        p4 += 1

    elif num >= 800:
        p5 += 1

print(f'{p1 / n * 100 :.2f}%')
print(f'{p2 / n * 100 :.2f}%')
print(f'{p3 / n * 100 :.2f}%')
print(f'{p4 / n * 100 :.2f}%')
print(f'{p5 / n * 100 :.2f}%')

# divide without remainder------------------------------------------------------
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

    if num % 4 == 0:  # separate if-s are needed as some will be dividable by all 3
        p3 += 1

print(f'{p1 / n * 100 :.2f}%')
print(f'{p2 / n * 100 :.2f}%')
print(f'{p3 / n * 100 :.2f}%')

# salary------------------------------------------------------------------------
tabs = int(input())
salary = int(input())

for i in range(0, tabs):
    website = input()

    if website == 'Facebook':
        salary -= 150

    elif website == 'Instagram':
        salary -= 100

    elif website == 'Reddit':
        salary -= 50

if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)

# ****************More exercises ***********************************************

# back to the past -----------------------------------------

inheritance = float(input())
year = int(input())
age = 17
total_expenses = 0

for y in range(1800, year+1):
    age += 1
    if y % 2 == 0:
        expenses = 12000
    else:
        expenses = 12000 + 50 * age

    # print(age)
    # print(expenses)
    # print(total_expenses)
    total_expenses += expenses
    inheritance -= expenses
    # print(inheritance)

if inheritance >= 0:
    print(f'Yes! He will live a carefree life and will have {abs(inheritance):.2f} dollars left.')
else:
    print(f'He will need {abs(inheritance):.2f} dollars to survive.')

# hospital----------------------------------------------------------------------

period = int(input())
total_treated = 0
total_untreated = 0
treated_patients = 0
untreated_patients = 0
doctors = 7

for day in range(1, period + 1):
    patients = int(input())

    if patients <= doctors:
        treated_patients += patients
    else:
        treated_patients += doctors
        untreated_patients += (patients - doctors)

    if day % 3 == 0 and untreated_patients >= treated_patients:
        doctors += 1
        treated_patients += 1
        untreated_patients -= 1

total_treated += treated_patients
total_untreated += untreated_patients
print(f'Treated patients: {total_treated}.')
print(f'Untreated patients: {untreated_patients}.')

# logistics---------------------------------------------------------------------

cargos = int(input())
bus = 0
shuttle = 0
train = 0
cargo_volume = 0
total_price = 0

for cargo in range(cargos):
    cargo_weight = int(input())

    if cargo_weight <= 3:
        bus += cargo_weight
        price = 200
        cargo_price = cargo_weight * price

    elif cargo_weight >= 4 and cargo_weight <= 11:
        shuttle += cargo_weight
        price = 175
        cargo_price = cargo_weight * price

    elif cargo_weight >= 12:
        train += cargo_weight
        price = 120
        cargo_price = cargo_weight * price

    cargo_volume += cargo_weight
    total_price += cargo_price

# print(cargo_volume)
# print(bus)
# print(shuttle)
# print(train)
print(f'{total_price/cargo_volume:.2f}')
print(f'{bus/cargo_volume * 100:.2f}%')
print(f'{shuttle/cargo_volume * 100:.2f}%')
print(f'{train/cargo_volume * 100:.2f}%')

# grades -----------------------------------------------------------------------

students = int(input())
excellent = 0
good = 0
average = 0
poor = 0
all_grades = 0

for student in range(students):
    grade = float(input())
    all_grades += grade

    if grade >= 2.00 and grade <= 2.99:
        poor += 1

    elif grade >= 3.00 and grade <= 3.99:
        average += 1

    elif grade >= 4.00 and grade <=4.99:
        good += 1

    else:
        excellent += 1

print(f'Top students: {excellent/students*100:.2f}%')
print(f'Between 4.00 and 4.99: {good/students*100:.2f}%')
print(f'Between 3.00 and 3.99: {average/students*100:.2f}%')
print(f'Fail: {poor/students*100:.2f}%')
print(f'Average: {all_grades/students:.2f}')


# game of intervals ------------------------------------------------------------

moves = int(input())
score = 0
zero_to_nine = 0
ten_to_nineteen = 0
twenty_to_twenty_nine = 0
thirty_to_thirty_nine = 0
forty_to_fifty = 0
invalid_numbers = 0

for move in range(moves):
    i = int(input())

    if i >= 0 and i <= 9:
        score += i * 0.20
        zero_to_nine += 1

    elif i >= 10 and i <= 19:
        score += i * 0.30
        ten_to_nineteen += 1

    elif i >= 20 and i <= 29:
        score += i * 0.40
        twenty_to_twenty_nine += 1

    elif i >= 30 and i <= 39:
        score += 50
        thirty_to_thirty_nine += 1

    elif i >= 40 and i <= 50:
        score += 100
        forty_to_fifty += 1

    elif i > 50 or i < 0:
        score /= 2
        invalid_numbers += 1

print(f'{score:.2f}')
print(f'From 0 to 9: {zero_to_nine/moves*100:.2f}%')
print(f'From 10 to 19: {ten_to_nineteen/moves*100:.2f}%')
print(f'From 20 to 29: {twenty_to_twenty_nine/moves*100:.2f}%')
print(f'From 30 to 39: {thirty_to_thirty_nine/moves*100:.2f}%')
print(f'From 40 to 50: {forty_to_fifty/moves*100:.2f}%')
print(f'Invalid numbers: {invalid_numbers/moves*100:.2f}%')

# bills ------------------------------------------------------------------------

periods = int(input())
water = 0
internet = 0
electricity = 0
other = 0

for period in range(periods):
    electricity_bill = float(input())

    electricity += electricity_bill
    water += 20
    internet += 15
    misc = (electricity_bill + 20 + 15) * 1.20

    other += misc
    total = electricity + water + internet + other

print(f'Electricity: {electricity:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f'Average: {total/periods:.2f} lv')

# footbal league ---------------------------------------------------------------

capacity = int(input())
fans = int(input())
A = 0
B = 0
V = 0
G = 0

for fan in range(fans):
    sector = input()

    if sector == 'A':
        A += 1

    elif sector == 'B':
        B += 1

    elif sector == 'V':
        V += 1

    elif sector == 'G':
        G += 1

    total = (A + B + V + G)

print(f'{A/fans*100:.2f}%')
print(f'{B/fans*100:.2f}%')
print(f'{V/fans*100:.2f}%')
print(f'{G/fans*100:.2f}%')
print(f'{total/capacity*100:.2f}%')


# Mock Exam 2019-10-27 bus stops ***********************************************

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

print(f'The final number of passengers is : {starting_passengers}')

# Admission Exam 2019-11-03 game info ******************************************

team = input()
games = int(input())

total_played = 0
avg_duration = 0
with_penalties = 0  # > 120
prolonged = 0       # > 90

for game in range(games):
    minutes = int(input())

    if minutes > 120:
        with_penalties += 1
        total_played += minutes

    elif minutes > 90 and minutes <= 120:
        prolonged += 1
        total_played += minutes

    else:
        total_played += minutes

    avg_duration = total_played/games

print(f"{team} has played {total_played} minutes. Average minutes per game: {avg_duration:.2f}")
print(f"Games with penalties: {with_penalties}")
print(f"Games with additional time: {prolonged}")

# Admission Exam 2019-07-28 seats **********************************************

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

# Admission Exam 2019-07-28 cruise games ***************************************

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


# Admission exam 2019-07-07 football tournament ********************************

team = input()
games = int(input())
game_count = 0
wins = 0
d = 0
losses = 0
points = 0

for game in range(games):
    outcome = input()
    game_count += 1

    if outcome == 'W':
        wins += 1
        points += 3

    elif outcome == 'D':
        d += 1
        points += 1

    else:
        losses += 1

    win_rate = wins/game_count*100

if games > 0:
    print(f"{team} has won {points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {d}")
    print(f"## L: {losses}")
    print(f"Win rate: {win_rate:.2f}%")

else:
    print(f"{team} hasn't played any games during this season.")

# Admission exam 2019=07-07 (pc game shop) *************************************

games_sold = int(input())
heartstone = 0
fornite = 0
overwatch = 0
others = 0

for game in range(games_sold):
    game_title = input()

    if game_title == 'Hearthstone':
        heartstone += 1

    elif game_title == 'Fornite':
        fornite += 1

    elif game_title == 'Overwatch':
        overwatch += 1

    else:
        others += 1

print(f"Hearthstone - {heartstone/games_sold*100:.2f}%")
print(f"Fornite - {fornite/games_sold*100:.2f}%")
print(f"Overwatch - {overwatch/games_sold*100:.2f}%")
print(f"Others - {others/games_sold*100:.2f}%")


# Admission exam 2019-06-16 Series *********************************************
budget = float(input())
film_series = int(input())
total_price = 0

for film in range(film_series):
    series_title = input()
    series_price = float(input())

    if series_title == 'Thrones':
        series_price *= 0.50

    elif series_title == 'Lucifer':
        series_price *= 0.60

    elif series_title == 'Protector':
        series_price *= 0.70

    elif series_title == 'TotalDrama':
        series_price *= 0.80

    elif series_title == 'Area':
        series_price *= 0.90

    total_price += series_price

left = abs(budget - total_price)

if total_price <= budget:
    print(f"You bought all the series and left with {left:.2f} lv.")
else:
    print(f"You need {left:.2f} lv. more to buy the series!")


# Admission exam 2019-06-16 Oscars *********************************************

actor = input()
academy_points = float(input())
judges = int(input())
points = 0
from_judge = 0
total_points = 0
is_enough = False

for judge in range(judges):
    judge_name = input()
    judge_points = float(input())

    points += len(judge_name) * judge_points / 2
    total_points = academy_points + points

    if total_points > 1250.5:
        is_enough = True
        break                     # program should end as soon as the points have been reached

if is_enough:
    print(f"Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {actor} you need {abs(1250.5-total_points):.1f} more!")

# Admission exam 2019-04-07 Movie Ratings **************************************

movies = int(input())
max_rating = 1
min_rating = 10
total_rating = 0
highest = ''
lowest = ''

for movie in range(movies):
    movie_title = input()
    rating = float(input())
    total_rating += rating

    if rating > max_rating:
        max_rating = rating
        highest = movie_title

    if rating < min_rating:
        min_rating = rating
        lowest = movie_title

    avg_rating = total_rating / movies

print(f"{highest} is with highest rating: {max_rating:.1f}")
print(f"{lowest} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {avg_rating:.1f}")

# Admission exam 2019-04-21 Easter Bake ****************************************

import math as m

pastries = int(input())
sugar = 0
flour = 0
max_sugar = -10000
max_flour = -10000

for pastry in range(pastries):
    sugar_used = int(input())        # 950 gram per packet
    flour_used = int(input())        # 750 gram per packet

    sugar += sugar_used
    flour += flour_used

    sugar_needed = m.ceil(sugar/950)
    flour_needed = m.ceil(flour/750)

    if sugar_used > max_sugar:
        max_sugar = sugar_used

    if flour_used > max_flour:
        max_flour = flour_used

print(f"Sugar: {sugar_needed}")
print(f"Flour: {flour_needed}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")

# Admission exam 2019-04-21 Easter Eggs ****************************************

eggs = int(input())
red = 0
orange = 0
blue = 0
green = 0

for egg in range(eggs):
    egg_colour = input()

    if egg_colour == 'red':
        red += 1

    elif egg_colour == 'orange':
        orange += 1

    elif egg_colour == 'blue':
        blue += 1

    elif egg_colour == 'green':
        green += 1

    max_eggs = max(red, orange, blue, green)

    if max_eggs == red:
        max_colour = "red"

    elif max_eggs == orange:
        max_colour = "orange"

    elif max_eggs == blue:
        max_colour = "blue"

    elif max_eggs == green:
        max_colour = "green"

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_eggs} -> {max_colour}")

# Admission Exam 2019-03-10 (Tennis Ranklist) **********************************

tournaments = int(input())
starting_points = int(input())
points = 0
wins = 0

for tournament in range(tournaments):
    reached = input()

    if reached == 'W':
        points += 2000
        wins += 1

    elif reached == 'F':
        points += 1200

    elif reached == 'SF':
        points += 720

    total_points = starting_points + points
    win_rate = wins/tournaments * 100

print(f"Final points: {total_points}")
print(f"Average points: {points//tournaments}")
print(f"{win_rate:.2f}%")

# Admission Exam 2019-03-10 (Fitness Center) *****************************************************************************

visitors = int(input())
back = 0
chest = 0
legs = 0
abs = 0
shake = 0
bar = 0

for visitor in range(visitors):
    activity = input()

    if activity == 'Back':
        back += 1

    elif activity == 'Chest':
        chest += 1

    elif activity == 'Legs':
        legs += 1

    elif activity == 'Abs':
        abs += 1

    elif activity == 'Protein shake':
        shake += 1

    elif activity == 'Protein bar':
        bar += 1

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{shake} - protein shake")
print(f"{bar} - protein bar")
print(f"{(back + chest + legs + abs)/visitors*100:.2f}% - work out")
print(f"{(shake + bar)/visitors*100:.2f}% - protein")
