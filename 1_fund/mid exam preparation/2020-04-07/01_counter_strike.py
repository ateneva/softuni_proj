
# ---------------------------------01. Counter Strike (Conditional Statements)---------------------------
# https://github.com/ateneva/softuni_proj/wiki/fund_20200407_mid_exam_retake

# ------------------- 100 points --------------------------

initial_energy = input()
enemy_distance = input()
battles = 0
left_energy = int(initial_energy)

while enemy_distance != 'End of battle':
    energy_used = int(enemy_distance)

    if left_energy < energy_used:
        print(f'Not enough energy! Game ends with {battles} won battles and {left_energy} energy')
        break
    else:
        left_energy -= energy_used
        battles += 1
        if battles % 3 == 0:
            left_energy += battles

    enemy_distance = input()
else:
    print(f"Won battles: {battles}. Energy left: {left_energy}" )
