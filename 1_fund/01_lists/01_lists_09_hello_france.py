
# ------------------------09. Hello, France (exam problem) ---------------------

'''
Create a program that calculates the profit after buying some items and selling them on a higher price.
In order to fulfil that, you are going to need certain data
    - you will receive a collection of items and a budget in the following format:
    {type->price|type->price|type->price……|type->price}
    {budget}


If a price for a certain item is higher than the maximum price, don’t buy it.
Every time you buy an item, you have to reduce the budget with the value of its price.
    If you don’t have enough money for it, you can’t buy it.
    Buy as much items as you can.

You have to increase the price of each of the items you have successfully bought with 40%.

Print the list with the new prices and the profit you will gain from selling the items. 
They need exactly 150$ for tickets for the train,
    so if their budget after selling the products is enough – print – "Hello, France!"
    and if not – "Time to go."

'''

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
