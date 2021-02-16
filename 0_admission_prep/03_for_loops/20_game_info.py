
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
