
# ---------------------------------01. Black Flag (Conditional Statements)-------------------------
# https://github.com/ateneva/softuni_proj/wiki/fund_20190806_mid_exam_retake

# ------- 100 points -----------------------
days = int(input())
daily_plunder = int(input())
target_plunder = float(input())
plunder = 0

for day in range(1, days + 1):
    plunder += daily_plunder

    if day % 3 == 0:
        plunder += daily_plunder * 0.50

    if day % 5 == 0:
        plunder -= plunder * 0.30

if plunder >= target_plunder:
    print(f"Ahoy! {plunder:.2f} plunder gained.")
else:
    print(f"Collected only {(plunder/target_plunder*100):.2f}% of the plunder.")

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

# ---------------------------------03. Man O War (Lists Advanced) -------------------------------------

# -----------100 points --------------------------

pirate = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
max_health = int(input())
command = input()
pirate_sinks = False
warship_sinks = False

while command != 'Retire':
    do = command.split(" ")[0]

    if do == "Fire":
        section = int(command.split(" ")[1])
        damage = int(command.split(" ")[2])
        if 0 <= section < len(warship):
            warship[section] -= damage
            if warship[section] <= 0:
                warship_sinks = True
                break

    elif do == "Defend":
        start = int(command.split(" ")[1])
        end = int(command.split(" ")[2])
        damage = int(command.split(" ")[3])

        if 0 <= start <= end < len(pirate):  # make sure both indexes are valid at the same time
            for p in range(start, end + 1):
                pirate[p] -= damage
                if pirate[p] <= 0:
                    pirate_sinks = True
                    break
        if pirate_sinks:
            break

    elif do == "Repair":
        section = int(command.split(" ")[1])
        health = int(command.split(" ")[2])

        if 0 <= section < len(pirate):
            pirate[section] += health
            if pirate[section] > max_health:
                pirate[section] = max_health

    elif do == "Status":
        need_repair = [section for section in pirate if section < max_health*0.20]
        print(f"{len(need_repair)} sections need repair.")

    command = input()

if warship_sinks:
    print("You won! The enemy ship has sunken.")

elif pirate_sinks:
    print("You lost! The pirate ship has sunken.")

else:
    print(f"Pirate ship status: {sum(pirate)}")
    print(f"Warship status: {sum(warship)}")
