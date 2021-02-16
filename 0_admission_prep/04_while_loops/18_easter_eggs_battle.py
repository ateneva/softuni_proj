
# ********* 04.Easter Eggs Battle (while loop) *********************************

first_player = int(input())
second_player = int(input())
battle = input()                                 # define string input outside the loop
problems = 0

while not battle == 'End of battle':             # program shuld end on input = "End of Battle" or when 1 player is out of eggs

    if battle == 'one':
        second_player -= 1

    elif battle == 'two':
        first_player -= 1

    if first_player == 0:                        # check if player 1 has run out of eggs
        print(f"Player one is out of eggs. Player two has {second_player} eggs left.")
        break

    if second_player == 0:                       # check if player 2 has run out of eggs
        print(f"Player two is out of eggs. Player one has {first_player} eggs left.")
        break

    battle = input()                             # add string input statement to ensure the loop ends

else:
    print(f"Player one has {first_player} eggs left.")
    print(f"Player two has {second_player} eggs left.")
