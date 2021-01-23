
# --------------------01. Softuni Reception (Conditional Statements)---------------------------
# # https://github.com/ateneva/softuni_proj/wiki/fund_20200705_mid_exam

# --------------------- 90 points --------------------------
questions = []
hours = 1

for i in range(1, 4):
    efficiency = int(input())
    questions.append(efficiency)

students = int(input())
queue = sum(questions)

while students > queue:
    students -=queue
    hours += 1

    if hours % 4 ==0:
        students -= 0
        hours += 1

print(f"Time needed: {hours}h.")
