
# ************************* 04.darts (while loop) ******************************

initial_score = int(input())
score_range = input()                             # define string input outside the loop
moves = 0

while not score_range == 'bullseye':              # program should end when someone hits the bullseye
    score = int(input())                          # define the last intger/float input inside the loop
    moves += 1

    if score_range == 'number section':
        initial_score -= score

    elif score_range == 'double ring':
        initial_score -= score * 2

    elif score_range == 'triple ring':
        initial_score -= score * 3

    if initial_score == 0:                        # check if a player has won by reaching 0 points
        print(f'Congratulations! You won the game in {moves} moves!')
        break

    if initial_score < 0:                         # check if a player has lost
        print(f"Sorry, you lost. Score difference: {abs(initial_score)}.")
        break

    score_range = input()                         # add string input statement to avoid conversion issues and to ensure the loop ends

else:
    print(f'Congratulations! You won the game with a bullseye in {moves+1} moves!')
