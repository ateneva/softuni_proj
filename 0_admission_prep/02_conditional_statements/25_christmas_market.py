
# ***********02.christmas market (condtional statements) ***********************

import math as m

target = float(input())
fantasy_books = int(input())
horror_books = int(input())
romantic_books = int(input())

revenue = fantasy_books * 14.90 \
            + horror_books * 9.80 \
            + romantic_books * 4.30

taxed_revenue = revenue * 0.80

if taxed_revenue > target:
    earned = m.floor((taxed_revenue-target) * 0.10)
    print(f"{(taxed_revenue-earned):.2f} leva donated.")
    print(f"Sellers will receive {earned} leva.")
else:
    print(f"{target-taxed_revenue:.2f} money needed.")
