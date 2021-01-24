
# -----------------Problem 03. Legendary Farming -------------------------------
# problem description

'''
You've done all the work and the last thing left to accomplish is to own a legendary item.
However, it's a tedious process and it requires quite a bit of farming.
Anyway, you are not too pretentious – any legendary item will do.

**The possible items are:**
* Shadowmourne – requires 250 Shards;
* Valanyr – requires 250 Fragments;
* Dragonwrath – requires 250 Motes;

**Shards, Fragments and Motes are the key materials** and everything **else is junk**.
You will be given lines of input, in the format:
`2 motes 3 ores 15 stones`

Keep track of the key materials - **the first one that reaches the 250 mark, wins the race.**
At that point you have to print that the corresponding legendary item is obtained.
Then, print the remaining shards, fragments, motes, ordered by quantity in descending order, then by name in ascending order, each on a new line.

Finally, print the collected junk items in alphabetical order.
## Input
* Each line comes in the following format: `{quantity} {material} {quantity} {material} … {quantity} {material}`

## Output
* On the first line, print the obtained item in the format: `{Legendary item}` obtained!
* On the next three lines, print the remaining key materials in descending order by quantity

If two key materials have the same quantity, print them in alphabetical order
* On the final several lines, print the junk items in alphabetical order

All materials are printed in format `{material}: {quantity}`
* The output should be **lowercase**, except for the first letter of the legendary
'''


key_materials = {
    "fragments": 0,
    "shards": 0,
    "motes": 0
}

legendary_items = {
    "fragments": "Valanyr",
    "shards": "Shadowmourne",
    "motes": "Dragonwrath"
}

junks = {}
winner = ''

while winner == '':
    args = input().lower().split()
    for i in range(0, len(args), 2):    # odd items represent materials, even items quantitites
        qty = int(args[i])
        material = args[i + 1]

        if material in key_materials:
            key_materials[material] += qty

            if key_materials[material] >= 250:   # the first material to reach 250 is winner
                winner = material
                break
        else:
            # junk
            if material not in junks:
                junks[material] = qty
            else:
                junks[material] += qty

key_materials[winner] -= 250    # key materials quantities must exclude winning quantity

print(f'{legendary_items[winner]} obtained!')

# order descending by value, ascending by key
key_materials = dict(sorted(key_materials.items(), key=lambda el: (-el[1], el[0])))
junks = dict(sorted(junks.items()))

for material, quantity in key_materials.items():
    print(f'{material}: {quantity}')

for material, quantity in junks.items():
    print(f'{material}: {quantity}')
