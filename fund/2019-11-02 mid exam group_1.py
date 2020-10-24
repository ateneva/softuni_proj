
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
