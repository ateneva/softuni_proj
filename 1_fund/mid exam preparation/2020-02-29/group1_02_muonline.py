
# https://github.com/ateneva/softuni_proj/wiki/fund_20200229_mid_exam_group_1

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
