
# # *********** 04.best plane tickets (while True loop) *************************
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


 #  approach 2

 # *********** 04.best plane tickets (while loop) ******************************

ticket = input()
min_delay = 501

while not ticket == 'End':
    price = float(input())     # define the last intger/float input inside the loop
    delay = int(input())       # define the last intger/float input inside the loop

    if delay < min_delay:
        min_delay = delay
        last_ticket = ticket
        last_price = price * 1.96
        hours = (delay // 60)
        minutes = delay % 60

    ticket = input()

else:
    print(f"Ticket found for flight {last_ticket} costs {last_price:.2f} leva with {hours}h {minutes}m stay")
