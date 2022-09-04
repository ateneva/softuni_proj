# walking ----------------------------------------------------------------------
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

# best plane tickets (exam 27th July 2019)--------------------------------------
import sys
import math as m

min_delay = sys.maxsize
hours = 0
minutes = 0

while True:
    ticket = input()
    if ticket == 'End':
        break
    ticket_price = float(input())
    delay = int(input())

    if delay < min_delay:
        min_delay = delay
        last_ticket = ticket
        last_price = ticket_price * 1.96
        hours = m.floor(delay/60)
        minutes = delay % 60

print(f'Ticket found for flight {last_ticket} costs {last_price:.2f} leva with {hours}h {minutes}m stay')
