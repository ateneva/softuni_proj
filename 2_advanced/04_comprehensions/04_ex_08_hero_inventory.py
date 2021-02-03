
# ---------------------------08. hero inventory ------------------------------

'''
Using comprehension write a program that receives some hero names and items
that need to be added in their inventory (item name and item cost).
Print the total amount of items with their total cost for each hero.

Input
    * On the first line you will receive hero names separated by comma and space ", "
    * On the next lines until the command "End", you will be given items with
        their cost in the following format: "{name}-{item}-{cost}".
        If an item already exists in a hero inventory - ignore it.
Output
    * For each hero print his name, the total items and the total item cost
     in the format: "{name} -> Items: {items_count}, Cost: {items_cost}"

'''

# approach 1: use a dictionay and list comprehension
def hero_inventory_one():
    heroes = input()
    items = input()
    heroes_inventory = {}

    while items != 'End':
        hero_names = heroes.split(", ")
        hero_items = items.split("-")
        hero_name = hero_items[0]
        item = hero_items[1]
        cost = int(hero_items[2])

        # add heroes to inventory
        if hero_name not in heroes_inventory.keys():
            heroes_inventory[hero_name] = []

        # skip items from inventory if already there
        if item not in heroes_inventory[hero_name]:
            heroes_inventory[hero_name].append(item)
            heroes_inventory[hero_name].append(cost)

        items = input()

    #print(heroes_inventory)
    for hero, obtained_items in heroes_inventory.items():

        inventory = len([i for i in obtained_items
                            if obtained_items.index(i) % 2 == 0])

        total_cost = sum([c for c in obtained_items
                            if obtained_items.index(c) % 2 != 0])

        print(f'{hero} -> Items: {inventory}, Cost: {total_cost}')

################################################################################

# appraoch 2:
        # step 1: build a dictionary within a dictionary
        # step 2: use a dictionary comprehension

def heroes_inventory():
    heroes = {name: {} for name in input().split(", ")}

    while True:
        hero_items = input().split("-")
        name = hero_items[0]

        if name == 'End':
            break

        item = hero_items[1]
        cost = int(hero_items[2])

        if item not in heroes[name]:
            heroes[name][item] = cost

    for name in heroes:
        inventory = len(heroes[name])
        total_cost = sum(heroes[name].values())
        print (f'{name} -> Items: {inventory}, Cost: {total_cost}')

if __name__ == '__main__':
    #hero_inventory_one()
    heroes_inventory()
