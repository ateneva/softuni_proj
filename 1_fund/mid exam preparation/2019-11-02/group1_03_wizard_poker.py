
# ************************************************ Group 1 ****************************************************
# https://github.com/ateneva/softuni_proj/wiki/fund_20191102_mid_exam_group_1

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
