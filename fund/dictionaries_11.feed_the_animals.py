
# 08. Feed the Animals (exam problem)--------------------------------------------------------
# --------------70 points ------------------------------------------
def print_dict(dictionary, template):
    for (key, value) in dictionary.items():
        print(template.format(key, value))

info = input()
animals = {}
areas = {}

while info != 'Last Info':
    info = info.split(':')
    activity = info[0]
    animal = info[1]

    if activity == 'Add':
        food_limit = int(info[2])
        area = info[3]

        if animal not in animals:
            animals[animal] = food_limit
        else:
            animals[animal] += food_limit

        if area not in areas:
            areas[area] = [animal]
        else:
            if animal not in areas[area]:
                areas[area].append(animal)

    elif activity == 'Feed':
        food = int(info[2])
        area = info[3]

        if animal in animals:
            animals[animal] -= food
            if animals[animal] <= 0:
                animals.pop(animal)
                areas[area].remove(animal)
                print(f"{animal} was successfully fed")

    info = input()

# print(animals, areas)
# sort descending by value and ascending by key
animals = dict(sorted(animals.items(), key=lambda x: (-x[1], x[0])))
areas = dict(sorted(areas.items(), key=lambda a: -len(areas)))

print('Animals:')
print_dict(animals, '{} -> {}g')
print('Areas with hungry animals:')
for k, v in areas.items():
    if len(v) > 0:
        print(f'{k} : {len(v)}')
