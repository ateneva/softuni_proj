
# game statistics (nested conditionals)----------------------------------------

minutes = int(input())
player = input()

if minutes == 0:
    print(f'Match has just began!')

elif minutes > 0 and minutes < 45:
    print(f'First half time.')

    if minutes >= 1 and minutes <= 10:
        print(f'{player} missed a penalty.')
        if minutes % 2 == 0:
            print(f'{player} was injured after the penalty.')

    elif minutes > 10 and minutes <= 35:
        print(f'{player} received yellow card.')
        if minutes % 2 != 0:
            print(f'{player} got another yellow card.')

    elif minutes > 35 and minutes < 45:
        print(f'{player} SCORED A GOAL !!!')

elif minutes >= 45:
    print(f'Second half time.')

    if minutes > 45 and minutes <= 55:
        print(f'{player} got a freekick.')
        if minutes % 2 == 0:
            print(f'{player} missed the freekick.')

    elif minutes > 55 and minutes <= 80:
        print(f'{player} missed a shot from corner.')
        if minutes % 2 != 0:
            print(f'{player} has been changed with another player.')

    elif minutes > 80 and minutes <= 90:
        print(f'{player} SCORED A GOAL FROM PENALTY !!!')
