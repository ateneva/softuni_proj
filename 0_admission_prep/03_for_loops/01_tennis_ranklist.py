
# ************** 05.tennis ranklist (for loop) ********************************

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
