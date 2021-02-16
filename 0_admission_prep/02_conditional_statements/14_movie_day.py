
 # **************** 02.movie day (conditional statements) **********************

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
