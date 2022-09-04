# 09. On the Way to Annapurna (exam problem) -----------------------------------

# --------------100 points ------------------------------------------
commands = input()
stores = {}

while commands != 'END':
    commands = commands.split('->')
    command = commands[0]
    store = commands[1]

    if command == 'Add':
        item = commands[2]
        if store not in stores:
            stores[store] = []

        if item.find(',') > 0:
            item = item.split(',')
            stores[store].extend(item)
        else:
            stores[store].append(item)

    elif command == 'Remove':
        if store in stores:
            stores.pop(store)

    commands = input()

# you need to sort both in descending
stores = dict(sorted(stores.items(), key=lambda s: s[0], reverse=True)) # (1) sort by key DESC
stores = dict(sorted(stores.items(), key=lambda s: -len(s[1])))         # (2) sort by value DESC

print('Stores list:')
for key, value in stores.items():
    print(key)
    for v in value:
        print(f'<<{v}>>')
