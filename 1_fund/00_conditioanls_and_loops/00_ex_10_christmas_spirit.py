# -------10. Christimas Spirit (exam problem)-----------------------------------
quantity = int(input())
days = int(input())

spirit = 0
cost = 0

for day in range(1, days + 1):

    if day % 11 == 0:          # increase quanity every 11th day
        quantity += 2          # must be in the beginning to ensure the new quantity is picked up

    if day % 2 == 0:           # every 2nd day, you buy sets
        cost += quantity * 2
        spirit += 5

    if day % 3 == 0:           # every 3rd day you buy skirts and garlands
        cost += quantity * 5
        cost += quantity * 3
        spirit += 13

    if day % 5 == 0:           # every 5th day, you buy lights
        cost += quantity * 15
        spirit += 17

        if day % 3 == 0:       # if you've bought skirts and garlands the same day
            spirit += 30

    if day % 10 == 0:          # you lose spirit every 10th day
        spirit -= 20
        cost += 5              # 1 piece of each
        cost += 3
        cost += 15

        if day == days:
            spirit -= 30       # last day is als0 10th data

# must be separate if s because a day can meet 2 conditions at the same time;
# with elif structure only the first condition will be executes

print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")
