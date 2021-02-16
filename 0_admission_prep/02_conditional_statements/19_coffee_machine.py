
 # ********* 03.coffee machine (nested condtiinal statements) ******************

drink = input()
sugar = input()
bought = int(input())
price = 0
discount = 0

if drink == 'Espresso':
    if sugar == 'Without':
        price = 0.90 * (1-0.35)
    elif sugar == 'Normal':
        price = 1.00
    elif sugar == 'Extra':
        price = 1.20

    if bought >= 5:
        discount = bought * price * 0.25

elif drink == 'Cappuccino':
    if sugar == 'Without':
        price = 1.00 * (1-0.35)
    elif sugar == 'Normal':
        price = 1.20
    elif sugar == 'Extra':
        price = 1.60

elif drink == 'Tea':
    if sugar == 'Without':
        price = 0.50 * (1-0.35)
    elif sugar == 'Normal':
        price = 0.60
    elif sugar == 'Extra':
        price = 0.70

total_price = (bought * price) - discount
if total_price > 15:
    total_price *= 0.80

print(f"You bought {bought} cups of {drink} for {total_price:.2f} lv.")
