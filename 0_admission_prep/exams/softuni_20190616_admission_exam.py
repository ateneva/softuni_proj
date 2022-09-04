
 # ****************01.series calculator (simple calculations) ******************
import math as m

series = input()
seasons = int(input())
episodes = int(input())
series_time = float(input())

ads_time = series_time * 0.20
extra_time = (seasons * 10)
total_time = m.floor(seasons * episodes * (series_time + ads_time) + extra_time)

print(f"Total time needed to watch the {series} series is {total_time} minutes.")

 # **************01.movie profit (simple calculations) *************************
movie = input()
days = int(input())
tickets = int(input())
ticket_price = float(input())
cinema_percent = int(input())

revenue = tickets * ticket_price * days
total_earned = revenue * (1-cinema_percent/100)

print(f"The profit from the movie {movie} is {total_earned:.2f} lv.")

 # ******* 02.lunch break (conditional statements) *****************************
 import math as m

series = input()
episode = int(input())
lunch = int(input())

lunching = lunch * 1/8
resting = lunch * 1/4

left = lunch - (lunching + resting)
minutes_left = m.ceil(abs(episode-left))

if left >= episode:
    print(f"You have enough time to watch {series} and left with {minutes_left} minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {minutes_left} more minutes.")

 # ****************02.movie day (conditional statements) ***********************

shooting_time = int(input())
scenes = int(input())
scene_time = int(input())

prep_time = shooting_time * 0.15
shooting = scenes * scene_time

total_time = prep_time + shooting
left = round(abs(shooting_time-total_time))

if total_time <= shooting_time:
    print(f"You managed to finish the movie on time! You have {left} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {left} minutes.")

 # *************03.film premiere (nested condtiinal statements) ****************

movie = input()
munchies = input()
tickets = int(input())
price = 0
bill = 0

if movie == 'John Wick':
    if munchies == 'Drink':
        price = 12
    elif munchies == 'Popcorn':
        price = 15
    elif munchies == 'Menu':
        price = 19

elif movie == 'Star Wars':
    if munchies == 'Drink':
        price = 18
    elif munchies == 'Popcorn':
        price = 25
    elif munchies == 'Menu':
        price = 30

    if tickets >= 4:
        price *= 0.70

elif movie == 'Jumanji':
    if munchies == 'Drink':
        price = 9
    elif munchies == 'Popcorn':
        price = 11
    elif munchies == 'Menu':
        price = 14

    if tickets == 2:
        price *= (1-0.15)

bill = price * tickets

print(f"Your bill is {bill:.2f} leva.")

 # ********03.movie destination (nested condtiinal statements) *****************

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

 # **************04.cinema (while loop) ****************************************

hall_size = int(input())
cinema_goers = input()                                  # all string input is defined outside the loop and then converted to integer
capacity = hall_size
total_cinema_goers = 0
total_revenue = 0

while not cinema_goers == 'Movie time!':                # program should end on input 'Movie time!' or when the hall has reached capacity
    cinema_goers = int(cinema_goers)
    capacity -= cinema_goers

    if cinema_goers % 3 == 0:
        revenue = (cinema_goers * 5) - 5
    else:
        revenue = cinema_goers * 5

    total_cinema_goers += cinema_goers
    total_revenue += revenue

    if capacity < 0:                                    # check if the hall has reached capacity
        print(f"The cinema is full.")
        print(f"Cinema income - {total_revenue-revenue} lv.")
        break

    cinema_goers = input()                              # add string input statement to avoid conversion issues and ensure the loop ends

else:
    print(f"There are {capacity} seats left in the cinema.")
    print(f"Cinema income - {total_revenue} lv.")

 # **************04.movie stars (while loop) ***********************************

budget = float(input())
actor = input()                                 # define string input outside the loop

while not actor == 'ACTION':                    # program should end with ACTION or when budget has reached 0

    if len(actor) <= 15:
        salary = float(input())                 # define the last intger/float input inside the loop

    else:
        salary = budget * 0.20

    budget -= salary

    if budget <= 0:                             # check if budget has been exhausted
        print(f"We need {abs(budget):.2f} leva for our actors.")
        break

    actor = input()                             # add string input statement to avoid conversion issues and ensure the loop ends

else:
    print(f"We are left with {budget:.2f} leva.")

 # *************05.series (for loop) *******************************************

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

 # ***********05.oscars (for loop) *********************************************

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

 # ********06.favourtite movie (nested loop) ***********************************

movie = input()
movies = 0
most_points = 0
best_movie = ''

while not movie == 'STOP':
    movies += 1
    points = 0   # needs to start over for every movie

    for char in movie:
        p = ord(char)
        points += p

        if p >= 97 and p <= 122:
            points -= 2*len(movie)

        elif p >= 65 and p <= 90:
            points -= len(movie)

    if points >= most_points:
        most_points = points
        best_movie = movie

    if movies >= 7:
        print("The limit is reached.")
        print(f"The best movie for you is {best_movie} with {most_points} ASCII sum.")
        break

    movie = input()

else:
    print(f"The best movie for you is {best_movie} with {most_points} ASCII sum.")

 # ************06.movie tickets (nested loop) **********************************

a1 = int(input())
a2 = int(input())
n = int(input())
ticket = ''

for i in range(a1, a2):
    for j in range(1, n):
        for k in range(1, n//2):
            ticket = chr(i) + '-' + str(j) + str(k) + str(i)

            if i % 2 != 0 \
                 and (i + j + k) % 2 != 0:
                 print(ticket)
