
'''
You will be given a matrix with 7 rows and 7 columns representing the dartboard.

Each of the two players starts with a score of 501 and they take turns to throw a dart – one throw for each player.

The score for each turn is deducted from the player’s total score.
The first player who reduces their score to zero or less wins the game.

You are going to receive the information for every throw on a separate line.
The coordinate information of a hit will be in the format: "({row}, {column})".

- If a player hits outside the dartboard, he does not score any points.
- If a player hits a number, it is deducted from his total.
- If a player hits a "D" the sum of the 4 corresponding numbers per column
    and row is doubled and then deducted from his total.

- If a player hits a "T" the sum of the 4 corresponding numbers per column
    and row is tripled and then deducted from his total.

- "B" is the bullseye. If a player hits it, he wins the game, and the program ends.
For example, if Peter hits position with coordinates (2, 1),
    he wins (23 + 2 + 9 + 18) * 2 = 104 points and they are deducted from his total.

Your job is to find who won the game and with how many turns.
You should print only one line containing the winner and his count of throws:
"{name} won the game with {count_turns} throws!"

'''

import re


def get_square_matrix(size):
    matrix = []
    for _ in range(size):
        row = [x for x in input().split()]
        matrix.append(row)
    return matrix


def get_bull_position(field):
    bull_position = []
    for f in field:
        for position in f:
            if position == 'B':
                bull_position = [field.index(f), f.index(position)]
    return bull_position


def is_valid(pos, n):
    r = pos[0]
    c = pos[1]
    return 0 <= r < n and 0 <= c < size

##############################################################################


# get players
players = input().split(", ")

player_one = 501
player_two = 501
winner = ''
turn = 0
throws_one = 0
throws_two = 0

# get dartboard and bulls eye
size = 7
dartboard = get_square_matrix(size)
bulls_eye = get_bull_position(dartboard)


def get_score(position, field):
    x = position[0]
    y = position[1]
    score = 0

    if is_valid(position, 7):
        right = int(field[x][6])
        left = int(field[x][0])
        up = int(field[0][y])
        down = int(field[6][y])

        field_value = field[x][y]

        if field_value == 'D':
            score += (right + left + up + down)
            score *= 2

        elif field_value == 'T':
            score += (right + left + up + down)
            score *= 3

        elif field_value not in ('T', 'D', 'B'):
            score += int(field_value)
    return score


while True:
    throw = input()
    valid_throw = [int(i) for i in re.findall(r"[0-9]", throw)]

    if is_valid(valid_throw, 7):
        player_score = get_score(valid_throw, dartboard)

        # calculate individual scores
        if turn % 2 == 0:
            throws_one += 1
            if bulls_eye == valid_throw:
                winner = players[0]
                break
            else:
                player_one -= player_score
                if player_one <= 0:
                    winner = players[0]
                    break
        else:
            throws_two += 1
            if bulls_eye == valid_throw:
                winner = players[1]
                break
            else:
                player_two -= player_score
                if player_two <= 0:
                    winner = players[1]
                    break
    # change turn
    turn += 1

if winner == players[0]:
    print(f'{winner} won the game with {throws_one} throws!')
else:
    print(f'{winner} won the game with {throws_two} throws!')
