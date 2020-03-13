
# ************************************************ Group 1 ****************************************************

# ---------------------------------01. Biscuits Factory (Conditional Statements)---------------------------

# ------- 100 points -----------------------

import math as m

biscuits_pw_pd = int(input())
workers = int(input())
competitor_pm = int(input())
biscuits = 0

for day in range(1, 31):
    biscuits_pd = biscuits_pw_pd * workers

    if day % 3 == 0:
        biscuits_pd = m.floor(biscuits_pd * 0.75)

    biscuits += biscuits_pd

print(f"You have produced {biscuits} biscuits for the past month.")
percentage = (biscuits-competitor_pm)/competitor_pm * 100

if biscuits > competitor_pm:
    print(f"You produce {percentage:.2f} percent more biscuits.")

else:
    print(f"You produce {abs(percentage):.2f} percent less biscuits.")


# ---------------------------------02. Weaponsmith (Lists Basic)---------------------------------------------

# ------- 100 points -----------------------

parts = input().split("|")
command = input()

while command != 'Done':
    do = command.split(" ")[0]
    #print(parts, command, do)

    if do == 'Move':
        direction = command.split(" ")[1]
        idx = int(command.split(" ")[2])
        old_idx = idx

        if idx < len(parts):
            if direction == 'Left':
                idx = idx-1
            elif direction == 'Right':
                idx = idx + 1

            if idx >= 0:
                to_move = parts.pop(old_idx)
                parts.insert(idx, to_move)

    elif do == 'Check':
        num_type = command.split(" ")[1]
        if num_type == 'Even':
            evens = [e for e in parts if parts.index(e) % 2 == 0]
            print(" ".join(evens))

        elif num_type == 'Odd':
            odds = [o for o in parts if parts.index(o) % 2 != 0]
            print(" ".join(odds))

    command = input()

weapon = "".join(parts)
print(f"You crafted {weapon}!")

# ---------------------------------03. Wizard Poker (Lists Advanced) ----------------------------------------

# ------- 100 points -----------------------

cards = input().split(":")
command = input()
my_deck = []

while command != "Ready":
    do = command.split(" ")[0]
    card = command.split(" ")[1]
    #print(cards, command)

    if do == "Add":
        if card in cards:
            my_deck.append(card)
        else:
            print("Card not found.")

    elif do == "Insert":
        idx = int(command.split(" ")[2])
        if card in cards:
            if idx >= 0 and idx < len(my_deck):
                my_deck.insert(idx, card)
            else:
                print("Error!")
        else:
            print("Error!")

    elif do == "Remove":
        if card in my_deck:
            my_deck.remove(card)
        else:
            print("Card not found.")

    elif do == "Swap":
        card_one = command.split(" ")[1]
        card_two = command.split(" ")[2]
        idx_one = my_deck.index(card_one)
        idx_two = my_deck.index(card_two)

        my_deck[idx_one], my_deck[idx_two] = my_deck[idx_two], my_deck[idx_one]

    elif do == "Shuffle":
        my_deck.reverse()

    command = input()

print(" ".join(my_deck))

# ************************************************ Group 2 ****************************************************

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

