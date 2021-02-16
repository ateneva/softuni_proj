
# ---------------------problem 09: bunkers ------------------------------------

'''
On the first line you will be given all item categories present in the bunker,
then you will be given a number (n).
On the next "n" lines you will be given different items in the following format:
    "{category} - {item_name} - quantity:{item_quantity};quality:{item_quality}".
    Store that information, you will need it later.
After you receive all the inputs, print the total amount of items
    (sum the quantities) in the format: "Count of items: {count}".

After that print the average quality of all items in the format:
    "Average quality: {quality sum/categories count}" - formatted to the 2nd digit.
Finally, print all categories with the items on separate lines in the format:
    "{category} -> {item1}, {item2}, …".

'''

categories = input().split(", ")
num = int(input())
storage ={}


for n in range(num):
    items = input().split(" - ")
    category = items[0]
    item_name = items[1]
    attributes = items[2].split(";")
    qty = int(attributes[0].split(":")[1])
    quality = int(attributes[1].split(":")[1])

    inventory = {item_name: (qty, quality) for a in attributes}
    #print(inventory)

    if category not in storage:
        storage[category] = inventory

    else:
        storage[category].update(inventory)

#print(storage)

categories_count = 0
items_count = 0
total_qaulity = 0

for cat, foods in storage.items():
    for f, i in foods.items():
        #print(f, i)
        items_count += i[0]
        total_qaulity +=i[1]
    categories_count +=1

print(f'Count of items: {items_count}')
print(f'Average quality: {total_qaulity/categories_count:.2f}')

for cat, foods in storage.items():
    food_types = []
    for f in foods.keys():
        food_types.append(f)
    print(f'{cat} -> {", ".join(food_types)}')
