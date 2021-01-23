
# ************************************************ Group 2 ****************************************************
# https://github.com/ateneva/softuni_proj/wiki/fund_20191102_mid_exam_group_2

# ---------------------------------03. Tanks Collector (Lists Advanced) -------------------------------------

# ------- 100 points -----------------------

owned = input().split(", ")
commands = int(input())

for c in range(1, commands + 1):
    command = input()
    do = command.split(", ")[0]
    #print(owned, command)

    if do == "Add":
        tank = command.split(", ")[1]
        if tank not in owned:
            owned.append(tank)
            print("Tank successfully bought")
        else:
            print("Tank is already bought")

    elif do == "Remove":
        tank = command.split(", ")[1]
        if tank in owned:
            owned.remove(tank)
            print("Tank successfully sold")
        else:
            print("Tank not found")

    elif do == "Remove At":
        idx = int(command.split(", ")[1])
        if idx >= 0 and idx < len(owned):
            del owned[idx]
            print("Tank successfully sold")
        else:
            print("Index out of range")

    elif do == "Insert":
        idx = int(command.split(", ")[1])
        tank = command.split(", ")[2]

        if idx >= 0 and idx < len(owned):
            if tank not in owned:
                owned.insert(idx, tank)
                print("Tank successfully bought")
            else:
                print("Tank is already bought")
        else:
            print("Index out of range")

print(", ".join(owned))
