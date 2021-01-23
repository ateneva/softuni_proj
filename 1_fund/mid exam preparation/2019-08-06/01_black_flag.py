
# ---------------------------------01. Black Flag (Conditional Statements)-------------------------
# https://github.com/ateneva/softuni_proj/wiki/fund_20190806_mid_exam_retake

# ------- 100 points -----------------------
days = int(input())
daily_plunder = int(input())
target_plunder = float(input())
plunder = 0

for day in range(1, days + 1):
    plunder += daily_plunder

    if day % 3 == 0:
        plunder += daily_plunder * 0.50

    if day % 5 == 0:
        plunder -= plunder * 0.30

if plunder >= target_plunder:
    print(f"Ahoy! {plunder:.2f} plunder gained.")
else:
    print(f"Collected only {(plunder/target_plunder*100):.2f}% of the plunder.")
