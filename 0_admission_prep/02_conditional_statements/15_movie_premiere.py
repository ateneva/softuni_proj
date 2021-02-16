

 # ***********03.film premiere (nested condtiinal statements) ******************

movie = input()
munchies = input()
tickets = int(input())
price = 0
bill = 0

if movie == 'John Wick':
    if munchies == 'Drink':
        price = 12
    elif munchies == 'Popcorn':
        price = 15
    elif munchies == 'Menu':
        price = 19

elif movie == 'Star Wars':
    if munchies == 'Drink':
        price = 18
    elif munchies == 'Popcorn':
        price = 25
    elif munchies == 'Menu':
        price = 30

    if tickets >= 4:
        price *= 0.70

elif movie == 'Jumanji':
    if munchies == 'Drink':
        price = 9
    elif munchies == 'Popcorn':
        price = 11
    elif munchies == 'Menu':
        price = 14

    if tickets == 2:
        price *= (1-0.15)

bill = price * tickets

print(f"Your bill is {bill:.2f} leva.")
