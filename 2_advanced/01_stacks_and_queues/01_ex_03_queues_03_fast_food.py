
# ----------------------Problem 3: Fast Food------------------------------------
# https://github.com/ateneva/softuni_proj/wiki/adv_queues_03_fast_food

# -----------100 points ---------------------
from collections import deque

food = int(input())
orders = deque(list(map(lambda x: int(x), input().split(' '))))
success = True

order_queue = deque(orders)
print(max(orders))

while orders:
    order = orders.popleft()
    if food >= order:
        food -= order
    else:
        success = False
        orders.appendleft(order)
        break

print_format = ' '.join(
    list(map(lambda x: str(x),orders))
    )

if success:
    print(f'Orders complete')
else:
    print(f'Orders left: {print_format}')
