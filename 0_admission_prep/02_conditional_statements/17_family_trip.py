

 # *********** 02.family trip (conditional statements) *************************

budget = float(input())
nights = int(input())
price_per_night = float(input())
unallocated = int(input())

if nights > 7:
    price = price_per_night * 0.95
else:
    price = price_per_night

misc = budget * (unallocated/100)
expenses = (nights * price) + misc

left = abs(expenses-budget)

if expenses <= budget:
    print(f"Ivanovi will be left with {left:.2f} leva after vacation.")

else:
    print(f"{left:.2f} leva needed.")
