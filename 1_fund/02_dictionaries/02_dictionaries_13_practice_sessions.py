
# -----------------------10. Practice Sessions (exam problem) ------------------

# -------100 points -------------------
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


# ******************************************* More Exercises ******************************************************
