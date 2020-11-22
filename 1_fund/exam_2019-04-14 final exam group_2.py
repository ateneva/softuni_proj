

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
