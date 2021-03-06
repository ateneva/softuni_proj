
# ************************************************ Group 1 ****************************************************

# ---------------------------------02. Hello France (Lists Basic)----------------------------------------------
# https://github.com/ateneva/softuni_proj/wiki/fund_20190310_mid_exam_group_1

# ------- 100 points -----------------------

items = input().split('|')
budget = float(input())
max_price = 0
earned = 0
spent = 0
bought = []

for item in items:
    clothing = item.split('->')[0]
    initial_price = float(item.split('->')[1])
    #print(clothing, initial_price)

    if clothing == 'Clothes':
        max_price = 50

    elif clothing == 'Shoes':
        max_price = 35

    elif clothing == 'Accessories':
        max_price = 20.50

    if budget >= initial_price:
        if initial_price <= max_price:
            bought.append(initial_price)
            budget -= initial_price
            spent += initial_price

for price in bought:
    price *= 1.40
    print(f'{price:.2f}', end=' ')
    earned += price

print()
print(f'Profit: {earned-spent:.2f}')

if (earned + budget) >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
