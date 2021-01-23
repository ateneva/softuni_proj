
# ************************************************ Group 1 ****************************************************
# https://github.com/ateneva/softuni_proj/wiki/fund_20190630_mid_exam_group_1

# ---------------------------------01. Distance Calculator (Conditional Statements)---------------------------

# ------- 100 points -----------------------

steps = int(input())
step_length_cm = float(input())
target_distance_m = int(input())
distance_steps = steps * step_length_cm
distance = 0

for step in range(1, steps + 1):
    if step % 5 == 0:
        distance_steps -= step_length_cm * 0.30

    distance = distance_steps/100           # convert to meters

percentage = distance/target_distance_m * 100
print(f"You travelled {percentage:.2f}% of the distance!")
