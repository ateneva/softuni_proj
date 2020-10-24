
# -------------------------01. Bonus Scoring System (Conditional Statements)-------------------------

# ------- 100 points -----------------------
import math as m

students = int(input())
lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
student_attendances = 0

# {total bonus} = {student attendances} / {course lectures} * (5 + {additional bonus})

for student in range(1, students + 1):
    attendances = int(input())

    total_bonus = attendances / lectures * (5 + additional_bonus)

    if total_bonus > max_bonus:
        max_bonus = total_bonus
        student_attendances = attendances

print(f"Max Bonus: {m.ceil(max_bonus)}.")
print(f"The student has attended {student_attendances} lectures.")


# ---------------------------------02. MuOnline (Lists Basic)---------------------------------------

# ------- 100 points -----------------------
health = 100
total_bitcoins = 0
dungeons = input().split("|")
best_room = 0
is_dead = False

for room in dungeons:
    finding = room.split(" ")[0]
    best_room +=1

    if finding == "potion":
        replenish = int(room.split(" ")[1])
        if (health + replenish) < 100:
            replenish = replenish
        else:
            replenish = (100-health)
        health += replenish
        print(f"You healed for {replenish} hp.")
        print(f"Current health: {health} hp.")

    elif finding == "chest":
        bitcoins = int(room.split(" ")[1])
        total_bitcoins += bitcoins
        print(f"You found {bitcoins} bitcoins.")

    else:
        monster = finding
        attack = int(room.split(" ")[1])
        health -= attack
        if health > 0:
            print(f"You slayed {monster}.")
        else:
            is_dead = True
            break

if is_dead:
    print(f"You died! Killed by {monster}.")
    print(f"Best room: {best_room}")
else:
    print("You've made it!")
    print(f"Bitcoins: {total_bitcoins}")
    print(f"Health: {health}")


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