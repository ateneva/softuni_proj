
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

# ***************************************** Group 2 ****************************************************

# -------------------------01. The Isle of Man TT Race (Regex/ Text Processing)-------------------------

# -------------------------100 points ------------------------------------------
import re

while True:
    info = input()
    coordinates_found = False

    racer_pattern = r"^[#$%*&][a-zA-Z]+[#$%*&]{1}"  # racer
    racer = re.findall(racer_pattern, info)
    if len(racer) > 0:
        r = racer[0]
        if r[0] == r[-1]:
            racer_name = r.replace('#', '').replace('$', '').replace('%', '').replace('*', '').replace('&', '').replace('=', '')
        else:
            racer_name = ''
    else:
        racer_name = ''

    geohashlength_pattern = r"[=]+[0-9]+"   # geohashcode length
    geohashl = re.findall(geohashlength_pattern, info)
    if len(geohashl) > 0:
        gl = int(geohashl[0].replace('=', ''))
    else:
        gl = 0

    geohashcode_start = info.find('!!')
    geohashcode = info[geohashcode_start+2:]
    decrypted = ''
    for g in geohashcode:
        decrypted += chr(ord(g)+gl)

    if racer_name != '':
        if gl > 0:
            if gl == len(geohashcode):
                coordinates_found = True
                print(f'Coordinates found! {racer_name} -> {decrypted}')
                break
            else:
                print('Nothing found!')
        else:
            print('Nothing found!')
    else:
        print('Nothing found!')

# -------------------------02. Practice Sessions (Dictionaries)-----------------------------------------

# --------------100 points ------------------------------------------
road_info = input()
roads = {}

while road_info != 'END':
    road_info = road_info.split('->')
    command = road_info[0]

    if command =='Add':
        road = road_info[1]
        racer = road_info[2]

        if road not in roads:
            roads[road] = [racer]
        else:
            roads[road].append(racer)

    elif command == 'Move':
        current_road = road_info[1]
        racer = road_info[2]
        next_road = road_info[3]

        for road in roads.keys():
            if road == current_road:
                if racer in roads[road]:
                    roads[road].remove(racer)
                    roads[next_road].append(racer)

    elif command == 'Close':
        road = road_info[1]
        if road in roads:
            roads.pop(road)

    road_info = input()

# sort descending by count of the items, key ascending
roads = dict(sorted(roads.items(), key=lambda r: (-len(r[1]), r[0])))

print('Practice sessions:')
for key, value in roads.items():
    print(key)
    for v in value:
        print(f'++{v}')