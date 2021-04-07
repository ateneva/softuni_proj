
'''
You will receive a list of the cutomers (numbers seperated by comma and space ", ")
and list of your taxis (numbers seperated by comma and space ", ").
    -- Each number from the customer list represents how much time it takes to drive the customer to his/her destination.
    -- Each number from the taxis list represents how much time they can drive, before they need to refill their tanks.
    -- Keep track of the total time passed to drive all the customers to their destinations (values of all customers).
    -- Each time you tend customers you should put the first customer in the last taxi until there are no customers left.

    - If the taxi can drive the customer to his/her destination, he does and
        - You must add the time passed to drive the customer to his/her destination to the total time.
        - Remove both the customer and the taxi.
    - If the taxi cannot drive the customer to his/her destination,
        leave the customer at the beginning of the queue and remove the taxi.

At the end if you have successfully driven all the customers to their destinations,
    print "All customers were driven to their destinations Total time: {total_time} minutes"

Otherwise, if you ran out of taxis and there are still some customers left print 
        "Not all customers were driven to their destinations Customers left: {left_customers joined by ", "}""
'''

from collections import deque

customers = deque([int(i) for i in input().split(", ")])
taxis = [int(i) for i in input().split(", ")]

#print(customers)
#print(taxis)

total_drive = 0
taxis_left = True

while customers:
    if len(taxis) > 0:
        customer = customers[0]
        taxi = taxis[-1]

        if taxi >= customer:
            total_drive += customer
            customers.popleft()
            taxis.pop()

        else:
            taxis.pop()
    else:
        taxis_left = False
        break

if len(customers) == 0:
    print("All customers were driven to their destinations")
    print(f'Total time: {total_drive} minutes')
else:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join([str(c) for c in customers])}')
