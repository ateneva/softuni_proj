
# ********************************************** Group 2 *********************************************************
# https://github.com/ateneva/softuni_proj/wiki/fund_20190310_mid_exam_group_2

# ---------------------------------01. The Hunting Games (Conditional Statements)---------------------------------

# ------- 100 points -----------------------

days = int(input())
players = int(input())
energy = float(input())
water_pp_pd = float(input())   # pre-calculate rations per person, per day outside the loop
food_pp_pd = float(input())    # pre-calculate rations per person, per day outside the loop

water = water_pp_pd * players * days
food = food_pp_pd * players * days
energy_left = True

for day in range(1, days + 1):
    energy_loss = float(input())
    energy -= energy_loss

    if energy <= 0:            # needs to be the first stement as energy can fall below 0 before replenishment
        energy_left = False
        break

    if day % 2 == 0:
        energy += energy * 0.05
        water -= water * 0.30

    if day % 3 == 0:
        energy += energy * 0.10
        food -= food / players

if energy_left:
    print(f"You are ready for the quest. You will be left with - {energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {food:.2f} food and {water:.2f} water.")
