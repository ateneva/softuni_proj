
# -------------------------01. Bonus Scoring System (Conditional Statements)-------------------------
# https://github.com/ateneva/softuni_proj/wiki/fund_20200229_mid_exam_group_1

# ------- 100 points -----------------------
import math as m

students = int(input())
lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
student_attendances = 0

# {total bonus} = {student attendances} / {course lectures} * (5 + {additional bonus})

for student in range(1, students + 1):
    attendances = int(input())

    total_bonus = attendances / lectures * (5 + additional_bonus)

    if total_bonus > max_bonus:
        max_bonus = total_bonus
        student_attendances = attendances

print(f"Max Bonus: {m.ceil(max_bonus)}.")
print(f"The student has attended {student_attendances} lectures.")
