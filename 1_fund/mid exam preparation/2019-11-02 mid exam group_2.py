
# ************************************************ Group 2 ****************************************************
# https://github.com/ateneva/softuni_proj/wiki/fund_20191102_mid_exam_group_2

# ---------------------------------01. Experience Gaining (Conditional Statements)---------------------------

# ------- 100 points -----------------------

needed_experience = float(input())
battles = int(input())
experience = 0
experience_gained = False

for battle in range(1, battles + 1):
    experience_per_battle = float(input())

    if battle % 3 == 0:
        experience_per_battle += experience_per_battle * 0.15

    if battle % 5 == 0:
        experience_per_battle -= experience_per_battle * 0.10

    experience += experience_per_battle

    if experience >= needed_experience:
        experience_gained = True
        break

if experience_gained:
    print(f"Player successfully collected his needed experience for {battle} battles.")
else:
    print(f"Player was not able to collect the needed experience, {abs(experience-needed_experience):.2f} more needed.")

# ---------------------------------02. Friendliest Maintenance (Lists Basic)---------------------------------

# ------- 100 points -----------------------

friends = input().split(", ")
command = input()

while command != "Report":
    do = command.split(" ")[0]
    #print(friends, command, do)

    if do == 'Blacklist':
        friend = command.split(" ")[1].strip()
        if friend in friends:
            old_friend = friend
            friend_idx = friends.index(friend)
            friends[friend_idx] = "Blacklisted"
            print(f"{old_friend} was blacklisted.")
        else:
            print(f"{friend} was not found.")

    elif do == "Error":
        friend_idx = int(command.split(" ")[1])
        friend = friends[friend_idx]

        if friend not in ("Blacklisted", "Lost"):
            old_friend = friend.strip()
            friends[friend_idx] = "Lost"
            print(f"{old_friend} was lost due to an error.")

    elif do == "Change":
        idx = int(command.split(" ")[1])
        new_name = command.split(" ")[2]

        if idx >= 0 and idx < len(friends):
            old_name = friends[idx].strip()
            friends[idx] = new_name
            print(f"{old_name} changed his username to {new_name}.")

    command = input()

blacklisted = friends.count("Blacklisted")
lost = friends.count("Lost")
print(f"Blacklisted names: {blacklisted}")
print(f"Lost names: {lost}")
print(" ".join(friends))

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
