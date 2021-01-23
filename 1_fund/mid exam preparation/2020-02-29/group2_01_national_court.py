
# --------------------01. National Court (Conditional Statements)---------------------------
# https://github.com/ateneva/softuni_proj/wiki/fund_20200229_mid_exam_group_2

# --------------------- 90 points --------------------------
questions = []
hours = 1

for i in range(1, 4):
    efficiency = int(input())
    questions.append(efficiency)

people = int(input())
queue = sum(questions)

while people >= queue:
    people -=queue
    hours += 1

    if hours % 4 == 0:
        people -= 0
        hours += 1

print(f"Time needed: {hours}h.")
