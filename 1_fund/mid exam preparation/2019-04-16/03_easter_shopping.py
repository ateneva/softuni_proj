
# ---------------------------------03. Easter Shopping (Lists Advanced) -------------------------------------
# https://github.com/ateneva/softuni_proj/wiki/fund_20190416_mid_exam_retake

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
