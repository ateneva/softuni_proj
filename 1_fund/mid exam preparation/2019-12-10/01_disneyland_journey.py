
# ---------------------------------01. Disneyland Journey (Conditional Statements)-------------------------
# https://github.com/ateneva/softuni_proj/wiki/fund_20191210_mid_exam_retake

# ------- 100 points -----------------------

journey_cost = float(input())
months = int(input())
saved = 0

for month in range(1, months + 1):
    if month > 1 and month % 2 != 0:
        saved -= saved*0.16

    if month % 4 == 0:
        saved += saved * 0.25

    saved += journey_cost * 0.25     # if at the end in brief; calc must be after ifs

if saved > journey_cost:
    print(f"Bravo! You can go to Disneyland and you will have {saved - journey_cost:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {abs(saved-journey_cost):.2f}lv. more.")
