
# ---------------------------------01. Easter Cozonacs (Conditional Statements)------------------------------

# ------- 100 points -----------------------

budget = float(input())
price_flour = float(input())

price_eggs = price_flour * 0.75
price_milk = (price_flour * 1.25) * 0.25

price_kozunak = price_flour + price_eggs + price_milk
kozunaci = 0
eggs = 0

while budget > price_kozunak:
    budget -= price_kozunak
    kozunaci += 1
    eggs += 3

    if kozunaci % 3 == 0:
        eggs -= kozunaci - 2

print(f"You made {kozunaci} cozonacs! Now you have {eggs} eggs and {budget:.2f}BGN left.")


# ---------------------------------02. Easter Gifts (Lists Basic)--------------------------------------------

# ------- 100 points -----------------------

gifts = input().split(' ')
wish = input()

while wish != 'No Money':
    tokens = wish.split(' ')

    if tokens[0] == 'OutOfStock':
        gift = tokens[1]
        for g in range(len(gifts)):
            if gifts[g] == gift:
               gifts[g] = 'None'           # ideally we want to remove it from the list

    if tokens[0] == 'Required':
        idx = int(tokens[2])
        if idx >= 0 and idx < len(gifts):  # check if the index is valid
            gifts[idx] = tokens[1]

    if tokens[0] == 'JustInCase':
        gifts[-1] = tokens[1]              # replace the last present with the current present

    wish = input()

result = []
for gift in gifts:
    if gift != 'None':
        result.append(gift)

print(' '.join(result))


# ---------------------------------03. Easter Shopping (Lists Advanced) -------------------------------------

# ------- 83 points /2 x incorrect answer/-----------

stores = input().split(" ")
actions = int(input())
iterations = 0

#print(stores)

while iterations < actions:
    activities = input().split(" ")
    command = activities[0]

    if command == 'Include':
        store = activities[1]
        stores.append(store)

    elif command == 'Visit':
        to_remove = int(activities[2])
        which = activities[1]

        if to_remove >= 0 and to_remove < len(stores):
            if which == 'first':
                del stores [0: to_remove]

            if which == 'last':
                del stores [-to_remove:]

    elif command == 'Prefer':
        preference_one = int(activities[1])
        preference_two = int(activities[2])

        if preference_one >= 0 and preference_one < len(stores):
            if preference_two>= 0 and preference_two < len(stores):
                stores[preference_one], stores[preference_two] = stores[preference_two], stores[preference_one]

    elif command == 'Place':
        idx = int(activities[2])
        store = activities[1]

        if idx >= 0 and idx < len(stores):
            stores.insert(idx + 1, store)

    #print(activities, command)

    iterations += 1

print("Shops left:")
print(" ".join(stores))