
# darts tournament (exam 27th July 2019)----------------------------------------

initial_score = int(input())
moves = 0

while initial_score > 0:
    score_range = input()
    score = int(input())
    moves += 1

    if score_range == 'bullseye':
        initial_score = 0

    elif score_range == 'number section':
        initial_score -= score

    elif score_range == 'double ring':
        initial_score -= score * 2

    elif score_range == 'triple ring':
        initial_score -= score * 3

    if initial_score == 0\
            and score_range != 'bullseye':
        print(f'Congratulations! You won the game in {moves} moves!')

    elif initial_score == 0 \
            and score_range == 'bullseye':
        print(f'Congratulations! You won the game with a bullseye in {moves} moves!')
        break

if initial_score != 0:
    print(f'Sorry, you lost. Score difference: {abs(0-initial_score)}.')


# ************* 04.darts tournament approach 2 *********************************

initial_score = int(input())
score_range = input()
moves = 0

while not score_range == 'bullseye':
   score = int(input())
   moves += 1

   if score_range == 'number section':
       initial_score -= score

   elif score_range == 'double ring':
       initial_score -= score * 2

   elif score_range == 'triple ring':
       initial_score -= score * 3

   if initial_score == 0:       # check if a player has won by reaching 0 points
       print(f'Congratulations! You won the game in {moves} moves!')
       break

   if initial_score < 0:        # check if a player has lost
       print(f"Sorry, you lost. Score difference: {abs(initial_score)}.")
       break

   score_range = input()        # prevent infintie loop

else:
   print(f'Congratulations! You won the game with a bullseye in {moves+1} moves!')
