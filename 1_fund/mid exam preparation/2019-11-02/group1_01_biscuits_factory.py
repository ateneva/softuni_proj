
# ************************************************ Group 1 ****************************************************
# https://github.com/ateneva/softuni_proj/wiki/fund_20191102_mid_exam_group_1

# ---------------------------------01. Biscuits Factory (Conditional Statements)---------------------------

# ------- 100 points -----------------------

import math as m

biscuits_pw_pd = int(input())
workers = int(input())
competitor_pm = int(input())
biscuits = 0

for day in range(1, 31):
    biscuits_pd = biscuits_pw_pd * workers

    if day % 3 == 0:
        biscuits_pd = m.floor(biscuits_pd * 0.75)

    biscuits += biscuits_pd

print(f"You have produced {biscuits} biscuits for the past month.")
percentage = (biscuits-competitor_pm)/competitor_pm * 100

if biscuits > competitor_pm:
    print(f"You produce {percentage:.2f} percent more biscuits.")

else:
    print(f"You produce {abs(percentage):.2f} percent less biscuits.")
