
 # *********** 02.lunch break (conditional statements) *************************

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
