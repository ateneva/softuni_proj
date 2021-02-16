
# ********* 02.Easter Party (conditional statements) ***************************

guests = int(input())
menu_price = float(input())
budget = float(input())

due = menu_price * guests

if guests >= 10 and guests <= 15:
    due *= 0.85

elif guests > 15 and guests <= 20:
    due *= 0.80

elif guests > 20:
    due *= 0.75

cake = budget * 0.10
total = due + cake

left = abs(budget - total)

if total <= budget:
    print(f"It is party time! {left:.2f} leva left.")
else:
    print(f"No party! {left:.2f} leva needed.")
