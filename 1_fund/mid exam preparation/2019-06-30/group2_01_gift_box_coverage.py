
# ************************************************ Group 2 ****************************************************
# https://github.com/ateneva/softuni_proj/wiki/fund_20190630_mid_exam_group_2

# ---------------------------------01. Gift Box Coverage (Conditional Statements)---------------------------

# ------- 100 points -----------------------
size = float(input())
total_paper = int(input())
single_sheet_cover = float(input())
sides = 6

total_area = size ** 2 * sides
area_covered = 0

for paper in range(1, total_paper + 1):
    if paper % 3 == 0:
        single_sheet = single_sheet_cover * 0.25
    else:
        single_sheet = single_sheet_cover

    area_covered += single_sheet

percentage = area_covered / total_area * 100
print(f"You can cover {percentage:.2f}% of the box.")
