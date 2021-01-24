
# --------------------------04. Orders -----------------------------------------

'''
Write a program that keeps information about products and their prices.
**Each product has a name, a price and a quantity.**

If the product doesn't exist yet, **add it with its starting quantity.**

If you receive a product, **which already exists:**
* increase its quantity by the input quantity
* and if its price is different, **replace the price as well.**

You will receive products' names, prices and quantities on new lines.
Until you receive the command **"buy"**, keep adding items.
When you do receive the command "buy", print the items with their names and total price of all the products with that name.

## Input
* Until you receive "buy", the products will be coming in the format: `"{name} {price} {quantity}"`.
* The product data is always delimited by a single space.

## Output
* Print information about each product in the following format: `"{productName} -> {totalPrice}"`
* Format the average grade to **the 2nd digit after the decimal separator**.
'''

prices = {}
quantities = {}
total_prices = {}

product = input()

while product != 'buy':
    product = product.split(" ")

    item = product[0]
    price = float(product[1])
    qty = int(product[2])

    # add product if it doesn't exist, else update qty
    if item not in quantities:
        quantities[item] = qty
    else:
        quantities[item] += qty

    # always use latest price
    prices[item] = price
    product= input()

# calculate total prices
for item, price in prices.items():
    total_price = price * quantities[item]

    if item not in total_prices:
        total_prices[item] = total_price
    else:
        total_prices[item] += total_price

# print total prices
for product, price in total_prices.items():
    print(f'{product} -> {price:.2f}')
