
# ---------------------------------01. Black Flag (Conditional Statements)-------------------------
# https://github.com/ateneva/softuni_proj/wiki/fund_20190806_mid_exam_retake

# ---------------------------------02. Treasure Hunt (Lists Basic)------------------------------------

# ------- 70 points -----------------------
loot = input().split("|")
command = input()
stolen = []

while command != "Yohoho!":
    do = command.split(" ")[0]

    if do == "Loot":
        treasure = command.split(" ")[1:]
        for t in treasure:
            if t not in loot:
                loot.insert(0, t)

    elif do == 'Drop':
        idx = int(command.split(" ")[1])
        if idx <= len(loot):
            item = loot.pop(idx)
            loot.append(item)

    elif do == "Steal":
        idx = int(command.split(" ")[1])
        stolen.extend(loot[-idx:])
        del loot[-idx:]

    command = input()

print(", ".join(stolen))

if len(loot) > 0:
    value = 0
    for l in loot:
        item_value = len(l)
        value += item_value
    avg_value = value/len(loot)
    print(f"Average treasure gain: {avg_value:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
