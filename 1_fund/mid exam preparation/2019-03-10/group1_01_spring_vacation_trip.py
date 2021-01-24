
# ************************************************ Group 1 ****************************************************
# https://github.com/ateneva/softuni_proj/wiki/fund_20190310_mid_exam_group_1

# --------------------01. Spring Vacation Trip (Conditional Statements)---------------------------

# ------- 100 points -----------------------

days = int(input())
budget = float(input())
people = int(input())
fuel_per_km = float(input())
food_pp = float(input())         # pre-calculate rations per person, per day outside the loop
room_pp = float(input())         # pre-calculate rations per person, per day outside the loop
expenses = 0
depleted_budget = False

if people > 10:
    hotel_expenses = days * people * room_pp * 0.75
else:
    hotel_expenses = days * people * room_pp

food_expenses = days * people * food_pp
expenses = food_expenses + hotel_expenses

for d in range(1, days + 1):
    travelled = float(input())
    travel_expenses = travelled * fuel_per_km

    expenses += travel_expenses

    if d % 3 == 0 or d % 5 == 0:
        expenses += (expenses * 0.40)

    if d % 7 == 0:
        expenses -= (expenses/people)

    if expenses > budget:
        depleted_budget = True
        break

if depleted_budget:
    print(f"Not enough money to continue the trip. You need {abs(expenses-budget):.2f}$ more.")
else:
    print(f"You have reached the destination. You have {abs(expenses-budget):.2f}$ budget left.")
