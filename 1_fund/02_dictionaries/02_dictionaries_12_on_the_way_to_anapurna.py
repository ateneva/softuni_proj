
# --------------09. On the Way to Annapurna (exam problem) ---------------------

'''
Create a program, that lists stores and the items that can be found in them.
You are going to be receiving commands with the information you need until you get the "End" command.
There are three possible commands:
* "Add->{Store}->{Item}"
    > Add the store and the item in your diary. If the store already exists, add just the item.

* "Add->{Store}->{Item},{Item1}…,{ItemN}"
    > Add the store and the items to your notes. If the store already exists in the diary – add just the items to it.

* "Remove->{Store}"
    > Remove the store and its items from your diary, if it exists.
In the end, print the collection sorted by the count of the items in descending order
    and then by the names of the stores, again, in descending order in the following format:
    Stores list:
    {Store}
    <<{Item}>>
    <<{Item}>>
    <<{Item}>>
    '''

# --------------100 points -----------------------------------------------------
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
