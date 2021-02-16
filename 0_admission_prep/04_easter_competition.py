
# ****************06.Easter Competition (nested loop) **************************

bakers = int(input())
max_points = 0
winner = ''

for b in range(bakers):
    baker = input()
    score = input()
    baker_points = 0

    while not score == 'Stop':
        score = int(score)
        baker_points += score
        score = input()

    else:
        print(f"{baker} has {baker_points} points.")
        if baker_points > max_points:
            max_points = baker_points
            winner = baker
            print(f"{winner} is the new number 1!")

print(f"{winner} won competition with {max_points} points!")
