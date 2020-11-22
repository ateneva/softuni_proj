
# ******************************************** 01.basketball equipment (simple calculations) *******************************************************************

training = int(input())

shoes = training * 0.60
sportswear = shoes * 0.80
ball = sportswear * 0.25
misc = ball * 0.20

total = training + shoes + sportswear + ball + misc
print(f'{total:.2f}')


# ******************************************** 01.tennis equipment (simple calculations) ***********************************************************************
import math as m

tennis_racket = float(input())
count_rackets = int(input())
count_trainers = int(input())

trainers = tennis_racket * (1/6)
total_rackets = count_rackets * tennis_racket
total_trainers = count_trainers * trainers
misc = (total_rackets + total_trainers) * 0.20

total = total_rackets\
        + total_trainers \
        + misc

self = m.floor(1/8 * total)
sponsors = m.ceil(7/8 * total)

print(f"Price to be paid by Djokovic {self}")
print(f"Price to be paid by sponsors {sponsors}")

# ******************************************** 02.football results (conditional statements) ********************************************************************


first_match = input()
second_match = input()
third_match = input()
wins = 0
drawn = 0
losses = 0

if first_match[0] > first_match[2]:
    wins += 1
elif first_match[0] == first_match[2]:
    drawn += 1
else:
    losses += 1

if second_match[0] > second_match[2]:
    wins += 1

elif second_match[0] == second_match[2]:
    drawn += 1
else:
    losses += 1

if third_match[0] > third_match[2]:
    wins += 1

elif third_match[0] == third_match[2]:
    drawn += 1
else:
    losses += 1

print(f"Team won {wins} games.")
print(f"Team lost {losses} games.")
print(f"Drawn games: {drawn}")

# ******************************************** 02.skeleton (conditional statements) ****************************************************************************

control_minutes = int(input())
control_seconds = int(input())
length = float(input())
seconds = int(input())

total_control_seconds = control_minutes * 60 + control_seconds
reduced_timing = (length / 120) * 2.5
marin = (length / 100 ) * seconds - reduced_timing

if marin <= total_control_seconds:
    print(f"Marin Bangiev won an Olympic quota!" )
    print(f"His time is {marin:.3f}.")
else:
    print(f"No, Marin failed! He was {abs(marin - total_control_seconds):.3f} second slower.")


# ******************************************** 03.gymnastics (nested condtiinal statements) ********************************************************************

country = input()
tool = input()
difficulty = 0
performance = 0

if country == 'Russia':
    if tool == 'ribbon':
        difficulty = 9.100
        performance = 9.400

    elif tool == 'hoop':
        difficulty = 9.300
        performance = 9.800

    elif tool == 'rope':
        difficulty = 9.600
        performance = 9.000

elif country == 'Bulgaria':
    if tool == 'ribbon':
        difficulty = 9.600
        performance = 9.400

    elif tool == 'hoop':
        difficulty = 9.550
        performance = 9.750

    elif tool == 'rope':
        difficulty = 9.500
        performance = 9.400

elif country == 'Italy':
    if tool == 'ribbon':
        difficulty = 9.200
        performance = 9.500

    elif tool == 'hoop':
        difficulty = 9.450
        performance = 9.350

    elif tool == 'rope':
        difficulty = 9.700
        performance = 9.150

score = (difficulty + performance)
percent = (20 - score) / 20 * 100

print(f"The team of {country} get {score:.3f} on {tool}.")
print(f"{percent:.2f}%")


# ******************************************** 03.world snooker championship (nested condtiinal statements) ****************************************************

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

# ******************************************** 04.number wars (while loop) *************************************************************************************

first_player = input()
second_player = input()
first = input()                             # define first player points as string input outside the loop
first_points = 0
second_points = 0

while first != 'End of game':               # program should end on "End of game or when there was a number war"
    first = int(first)
    second = int(input())                   # define the last intger/float input inside the loop 

    if first > second:
        first_points += (first - second)

    elif first < second:
        second_points += (second - first)

    elif first == second:                   # check the outcome of a number war
        first = int(input())
        second = int(input())

        if first > second:
            winner = first_player
            points = first_points
        else:
            winner = second_player
            points = second_points
        print(f"Number wars!")
        print(f"{winner} is winner with {points} points")
        break

    first = input()                        # add string input statement for the first points to avoid conversion issues and to ensure the loop ends

else:
    print(f"{first_player} has {first_points} points")
    print(f"{second_player} has {second_points} points")


# ******************************************** 04.darts (while loop) *******************************************************************************************
initial_score = int(input())
score_range = input()                             # define string input outside the loop
moves = 0

while not score_range == 'bullseye':              # program should end when someone hits the bullseye
    score = int(input())                          # define the last intger/float input inside the loop
    moves += 1

    if score_range == 'number section':
        initial_score -= score

    elif score_range == 'double ring':
        initial_score -= score * 2

    elif score_range == 'triple ring':
        initial_score -= score * 3

    if initial_score == 0:                        # check if a player has won by reaching 0 points
        print(f'Congratulations! You won the game in {moves} moves!')
        break

    if initial_score < 0:                         # check if a player has lost
        print(f"Sorry, you lost. Score difference: {abs(initial_score)}.")
        break

    score_range = input()                         # add string input statement to avoid conversion issues and to ensure the loop ends

else:
    print(f'Congratulations! You won the game with a bullseye in {moves+1} moves!')


# ******************************************** 05.tennis ranklist (for loop) ***********************************************************************************

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


# ******************************************** 05.fitness center (for loop) ************************************************************************************

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


# ******************************************** 06.high jump (nested loop) **************************************************************************************
target = int(input())
first_target = target - 30
jumps = 0
fail = 0

while first_target <= target:
    for attempt in range(1, 4):
        next_jump = int(input())
        jumps += 1

        if next_jump > first_target:
            first_target += 5
            fail = 0
            break
        else:
            fail += 1

    if fail == 3:
        print(f"Tihomir failed at {next_jump}cm after {jumps} jumps.")
        break

else:
    print(f"Tihomir succeeded, he jumped over {target}cm after {jumps} jumps.")


# ******************************************** 06.basketball tournament (nested loop) **************************************************************************

tournament = input()
wins = 0
losses = 0
tournaments = 0

while tournament != 'End of tournaments':
    games = int(input())
    game_count = 0

    for game in range(1, games + 1):
        team_dessy = int(input())
        rival = int(input())
        game_count += 1
        winner_points = abs(team_dessy-rival)

        if team_dessy > rival:
            wins += 1
            print(f"Game {game_count} of tournament {tournament}: win with {winner_points} points.")

        else:
            losses += 1
            print(f"Game {game_count} of tournament {tournament}: lost with {winner_points} points.")

    tournaments += game_count
    tournament = input()

else:
    print(f'{(wins/tournaments * 100):.2f}% matches win')
    print(f'{(losses/tournaments * 100):.2f}% matches lost')