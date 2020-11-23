
# --------------------Problem 4 Fashion Boutique -------------------------------
# https://github.com/ateneva/softuni_proj/wiki/adv_stacks_04_fashion_boutique

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
