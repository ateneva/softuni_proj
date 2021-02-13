
# ----------------------Problem 3: Fast Food------------------------------------
# https://github.com/ateneva/softuni_proj/wiki/adv_queues_03_fast_food

'''
You have a fast food restaurant and most of the food that you're offering is
previously prepared. You need to know if you will have enough food to serve
lunch to all your customers.

Write a program that checks the orders' quantity.
You also want to know the client with the biggest order for the day

First, you will be given the quantity of the food that you have for the day.
Next, you will be given a sequence of integers, each representing the quantity of an order.

Keep the orders in a queue.
Find the biggest order and print it.
You will begin servicing your clients from the first one that came.

Before each order, check if you have enough food left to complete it.
If you have, remove the order from the queue and reduce the amount of food you have.
    If you succeeded in servicing all your clients, print: "Orders complete".
    If not, print: "Orders left: {order1} {order2} .... {orderN}".

'''

# -----------100 points ---------------------
from collections import deque

food = int(input())
orders = deque(list(map(lambda x: int(x), input().split(' '))))
success = True

order_queue = deque(orders)
print(max(orders))

while orders:
    order = orders.popleft()        # take the current order
    if food >= order:
        food -= order
    else:
        success = False
        orders.appendleft(order)    # keep the last remaining order
        break

print_format = ' '.join(
    list(map(lambda x: str(x),orders))
    )

if success:
    print(f'Orders complete')
else:
    print(f'Orders left: {print_format}')
