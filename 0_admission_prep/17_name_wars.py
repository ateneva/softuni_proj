
# name wars---------------------------------------------------------------------
winner = None
winner_sum = 0
sum = 0

while True:
    name = input()

    if name == 'STOP':
        break

    for char in name:
        sum += ord(char)

    if sum >= winner_sum:
        winner_sum = sum
        winner = name

    sum = 0

print(f'Winner is {winner} - {winner_sum}!')
