
# Problem statement in
# https://github.com/ateneva/softuni_proj/wiki/fund_lists_09.hello_france

# ------------------------09. Hello, France (exam problem) -----------------------------------------------------

items = input().split('|')
budget = float(input())
max_price = 0
earned = 0
spent = 0
bought = []

#print(items)

for item in items:
    clothing = item.split('->')[0]
    initial_price = float(item.split('->')[1])
    #print(clothing)
    #print(initial_price)

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

#print(bought)

for price in bought:
    price *= 1.40
    print(f'{price:.2f}', end=' ')
    earned += price

print()
#print(earned)
print(f'Profit: {earned-spent:.2f}')

if (earned + budget) >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
