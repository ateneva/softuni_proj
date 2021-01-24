
# -----------------------10. Practice Sessions (exam problem) ------------------

'''
Write a program, that keeps information about roads and the racers who practice on them.
When the practice begins, you’re going to start receiving data until you get the "END" message.
There are three possible commands:
*  "Add->{road}->{racer}"
    > Add the road if it doesn't exist in your collection and add the racer to it.

* "Move->{currentRoad}->{racer}->{nextRoad}"
    > Find the racer on the current road and move him to the next one, only if he exists in the current road.
    Both roads will always be valid and will already exist.

*  "Close->{road}"
    >  Find the road and remove it from the sessions, along with the racers on it if it exists.

In the end, print all of the roads with the racers who have practiced and ordered by
    * the count of the racers in descending order,
    * then by the roads in ascending order.

The output must be in the following format:
    Practice sessions:
    {road}
    ++{racer}
    ++{racer}
'''

# --------------------------100 points ----------------------------------------
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
