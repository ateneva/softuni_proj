
# Admission exam 2019=07-07 (pc game shop) ************************************

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
