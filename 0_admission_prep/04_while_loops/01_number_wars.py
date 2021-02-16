
# ************ 04.number wars (while loop) *************************************

first_player = input()
second_player = input()
first = input()                             # define first player points as string input outside the loop
first_points = 0
second_points = 0

while first != 'End of game':               # program should end on "End of game or when there was a number war"
    first = int(first)
    second = int(input())                   # define the last intger/float input inside the loop

    if first > second:
        first_points += (first - second)

    elif first < second:
        second_points += (second - first)

    elif first == second:                   # check the outcome of a number war
        first = int(input())
        second = int(input())

        if first > second:
            winner = first_player
            points = first_points
        else:
            winner = second_player
            points = second_points
        print(f"Number wars!")
        print(f"{winner} is winner with {points} points")
        break

    first = input()                        # add string input statement for the first points to avoid conversion issues and to ensure the loop ends

else:
    print(f"{first_player} has {first_points} points")
    print(f"{second_player} has {second_points} points")
