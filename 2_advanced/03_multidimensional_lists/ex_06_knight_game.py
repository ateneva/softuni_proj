
'''
The knight moves to the nearest square but not on the same row, column, or diagonal.
(This can be thought of as
    - moving two squares horizontally,
    - then one square vertically, or moving one square horizontally
    - then two squares vertically - i.e. in an "L" pattern.)
The knight game is played on a board with dimensions N x N.
You will receive a board with K for knights and '0' for empty cells.
Your task is to remove knights until there are no knights left that can attack one another.

Input
- On the first line, you will receive the N size of the board
- On the next N lines, you will receive strings with Ks and 0s.

Output
Print a single integer with the minimum number of knights that needs to be removed

'''

def get_board(board_size):
    board = []
    for _ in range(board_size):
        board_line = [x for x in input()]
        board.append(board_line)
    return board

def is_valid(pos, size):
    row = pos[0]
    col = pos[1]

    # check the indexes are within bounds
    within_bounds = 0 <= row < size and 0 <= col < size
    return within_bounds

def get_killed_knights(row, col, board_size, board):
    killed_knights = 0
    rows = [-2, -1, 1, 2, 2, 1, -1, -2]
    cols = [1, 2, 2, 1, -1, -2, -2, -1]

    # a knight can hit max 8 positions
    for i in range(8):
        current_pos = [row + rows[i], col + cols[i]]

        # check if the current postion is within the board
        if is_valid(current_pos, board_size) \
                and board[current_pos[0]][current_pos[1]]:   # check if there is a knight on current position
            killed_knights += 1
    return killed_knights


##########################################################################

n = int(input())
board = get_board(n)
total_kills = 0
for b in board:
    print(b)

max_kills = 0
to_kill = []

while True:
    max_kills = 0
    for row in range(n):
        for col in range(n):
            if board[row][col] == 'K':
                killed_knights = get_killed_knights(row, col, n, board)

                if killed_knights > max_kills:
                    max_kills = killed_knights
                    to_kill = [row, col]

    if max_kills == 0:
        break

    to_kill_row = to_kill[0]
    to_kill_col = to_kill[1]
    board[to_kill_row][to_kill_col] = "0"
    total_kills += 1

print(total_kills)
