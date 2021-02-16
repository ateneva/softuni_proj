
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
