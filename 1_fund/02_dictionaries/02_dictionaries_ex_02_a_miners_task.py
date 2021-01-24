
# -----------------------Problem 02. A miner's task ----------------------------

'''
You will be given a sequence of strings, each on a new line.
Every odd line on the console is representing a resource (e.g. Gold, Silver, Copper, and so on)
    and every even – quantity.

Your task is to collect the resources and print them each on a new line.
Print the resources and their quantities in the following format:
    {resource} –> {quantity}
'''

resources = {}

while True:
    resource = input()
    if resource == 'stop':
        break

    quantity = int(input())

    if resource not in resources:
        resources[resource] = quantity
    else:
        resources[resource] += quantity

for resource, quantity in resources.items():
    print(f'{resource} -> {quantity}')
