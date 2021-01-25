
# ------------------------------04. orders -------------------------------------

'''
Write a function that calculates the total price of an order and prints it on the console.
The function should receive one of the following products:
    coffee, coke, water, snacks; and a quantity of the product.

The prices for a single piece of each product are:
    * coffee - 1.50
    * water - 1.00
    * coke - 1.40
    * snacks - 2.00
Print the result formatted to the second decimal place.
'''

# --------------100 points --------------------
product = input()
qty = int(input())

def bill(product, qty):
    if product == 'coffee':
        return qty * 1.50

    elif product == 'water':
        return qty * 1.00

    elif product == 'coke':
        return qty * 1.40

    elif product == 'snacks':
        return qty * 2.00

print(f'{bill(product, qty):.2f}')
