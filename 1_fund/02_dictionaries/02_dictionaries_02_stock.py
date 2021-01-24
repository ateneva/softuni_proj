
# -----------------------------------02.stock --------------------------------------------------

'''
After you have successfully completed your first task, your boss decides to give you another one right away.
Now not only you have to keep track of the stock,
but also you have to answer customers if you have some products in stock or not.

You will be given key-value pairs of products and quantities (on a single line separated by space).
On the next line you will be given products to search for. Check for each product, you have 2 possibilities:
    • If you have the product, print "We have {quantity} of {product} left"
    • Otherwise, print "Sorry, we don't have {product}"
'''

def stock(recipe, products):
    bake = recipe.split(' ')
    search = products.split(' ')
    bakery = {}

    #print(bakery, search)

    for b in range(0, len(bake), 2):
        key = bake[b]
        value = bake[b + 1]
        bakery[key] = int(value)

    for product in search:
        if product in bakery:
            quantity = bakery[product]
            print(f"We have {quantity} of {product} left")
        else:
            print(f"Sorry, we don't have {product}")

stock(input(), input())
