
# walking ---------------------------------------------------------------------
target = 10000
total_steps = 0

while True:
    steps = input()
    if steps == 'Going home':
        steps = int(input())
        total_steps += steps

        if total_steps >= target:
            print('Goal reached! Good job!')
            break                               # don't forget to break
        else:
            more = abs(total_steps - target)
            print(f'{more} more steps to reach goal.')
            break

    elif steps != 'Going home':
        steps = int(steps)
        total_steps += steps
        if total_steps >= target:
            print('Goal reached! Good job!')
            break
