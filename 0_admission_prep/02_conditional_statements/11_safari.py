

# ************** 02.safari (conditional statements) ****************************

budget = float(input())
petrol_needed = float(input())
day = input()

petrol = petrol_needed * 2.10
total = petrol + 100

if day == 'Saturday':
    total *= 0.90
else:
    total *= 0.80

left = abs(budget-total)

if total <= budget:
    print(f"Safari time! Money left: {left:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {left:.2f} lv.")
