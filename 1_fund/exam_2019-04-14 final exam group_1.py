
# ***************************************** Group 1 ****************************************************

# -------------------------01. Arriving in Katmandu (Regex/ Text Processing)---------------------------

# --------------------40 points -------------------------------
import re
info = input()

while info != 'Last note':
    coordinates_found = False

    # peak name
    peak_pattern = r"\w[!@#$?a-zA-Z0-9]+[=]"
    peak = re.findall(peak_pattern, info)
    if len(peak) > 0:
        peak_name = peak[0].replace('!', '').replace('@', '').replace('#', '').replace('$', '').replace('?','').replace('=', '')
    else:
        peak_name = ''

    # geohashcode length
    geohashlength_pattern = r"[=]+[0-9]+"
    geohashl = re.findall(geohashlength_pattern, info)
    if len(geohashl) > 0:
        gl = int(geohashl[0].replace('=', ''))
    else:
        gl = 0

    # geohashcode
    geohashcode_pattern = r"[<<]+[a-z[0-9]+"
    geohashcode = re.findall(geohashcode_pattern, info)[0].replace('<<', '')

    if peak_name != '':
        if gl > 0:
            if gl == len(geohashcode):
                coordinates_found = True

    if coordinates_found:
        print(f'Coordinates found! {peak_name} -> {geohashcode}')
    else:
        print('Nothing found!')

    info = input()

# -------------------------02. On the Way to Anapurna (Dictionaries)-----------------------------------

# ----------------------100 points ---------------------------------------
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
