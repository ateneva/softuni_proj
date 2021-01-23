
# https://github.com/ateneva/softuni_proj/wiki/fund_20200229_mid_exam_group_2

# --------------------03. Heart Delivery (Lists Advances)---------------------------
# ------------------- 100 points --------------------------

houses = list(map(lambda x: int(x),input().split('@')))
command = input()
last_index = 0

while command != 'Love!':
    command = command.split(' ')
    activity = command[0]
    length = int(command[1])
    jump = last_index + length
    round = len(houses)

    if jump >= len(houses):
        jump = 0

    house = houses[jump]
    if house == 0:
        print(f"Place {jump} already had Valentine's day.")
    else:
        houses[jump] -= 2
        if houses[jump] == 0:
            print(f"Place {jump} has Valentine's day.")

    last_index = jump
    command = input()

print(f"Cupid's last position was {last_index}.")
if sum(houses) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len([f for f in houses if f > 0])} places.")
