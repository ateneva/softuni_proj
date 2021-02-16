

 # ***************** 06.name game (nested loop)*********************************

player = input()
winner_points = 0
winner = ''

while player != 'Stop':
    points = 0

    for char in player:
        i = ord(char)
        num = int(input())

        if i == num:
            points += 10
        else:
            points += 2

    if points >= winner_points:
        winner_points = points
        winner = player

    player = input()

print(f"The winner is {winner} with {winner_points} points!")
