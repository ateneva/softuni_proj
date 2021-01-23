
# https://github.com/ateneva/softuni_proj/wiki/fund_20200229_mid_exam_group_1

# ---------------------------------03. Inventory (Lists Advanced)------------------------------------

# ------- 100 points -----------------------
inventory = input().split(", ")
command = input()

while command != "Craft!":
    command = command.split(" - ")
    do = command[0]

    #print(inventory, command, do)

    if do == "Collect":
        item = command[1]
        if item not in inventory:
            inventory.append(item)

    elif do == "Drop":
        item = command[1]
        if item in inventory:
            inventory.remove(item)

    elif do == "Combine Items":
        items = command[1].split(":")
        old_item = items[0]
        new_item = items[1]
        if old_item in inventory:
            idx = inventory.index(old_item)
            inventory.insert(idx + 1, new_item)

    elif do == "Renew":
        item = command[1]
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)

    command = input()

print(", ".join(inventory))
