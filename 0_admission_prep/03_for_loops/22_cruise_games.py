
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
