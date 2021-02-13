
# --------------------Problem 4 Fashion Boutique -------------------------------
# https://github.com/ateneva/softuni_proj/wiki/adv_stacks_04_fashion_boutique

'''
You own a fashion boutique and you receive a delivery once a month in a huge box,
which is full of clothes. You must arrange them in your store, so you take the box
and start from the last piece of clothing on the top of the pile to the first one at the bottom.

Use a stack for the purpose. Each piece of clothing has its value (an integer).
You must sum their values, while you take them out of the box.
You will be given an integer representing the capacity of a rack.
    While the sum of the clothes is less than the capacity, keep summing them.
    If the sum becomes equal to the capacity you must take a new rack for the next clothes,
        if there are any left in the box.

    If it becomes greater than the capacity,
        don't add the piece of clothing to the current rack and take a new one.

In the end, print how many racks you have used to hang must the clothes.
'''

# ----------100 points-------------------------

clothes = [int(c) for c in input().split(' ')]
clothes_value = sum(clothes)
rack_capacity = int(input())
racks = 1

rack = []

while clothes:
    last_item = clothes[-1]
    full_rack = sum(rack) + last_item

    if rack_capacity >= full_rack:
        item = clothes.pop()
        rack.append(item)

    else:
        racks += 1
        rack.clear()

else:
    print(racks)
