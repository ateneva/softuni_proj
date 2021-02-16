
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
