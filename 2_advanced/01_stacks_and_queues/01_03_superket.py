
#------------------Problem 3 (queue): Supermarket-------------------------------

'''
Write a program that reads an input consisting of a name and adds it to a queue
until "End" is received.
If you receive "Paid",
    print every customer name and empty the queue,
    otherwise we receive a client and we must add him to the queue.

When we receive "End", we must print the count of the remaining people
in the queue in the format: "{count} people remaining."

'''

from collections import deque
queue = deque()

while True:
    customer = input()

    if customer == 'End':
        print(f'{len(queue)} people remaining.')
        break

    elif customer == 'Paid':
        # print customers in queue
        while queue:
            print(queue.popleft())

    else:
        # print remaining people
        queue.append(customer)
