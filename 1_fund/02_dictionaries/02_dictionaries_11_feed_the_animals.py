
# ---------------08. Feed the Animals (exam problem)---------------------------

'''
The sanctuary needs to provide food for the animals and feed them, so your task is to help with the process
Create a program that organizes the daily feeding of animals.
You need to keep information about animals, their daily food limit and the areas of the Wildlife Refuge they live in.
You will be receiving lines with commands until you receive the "Last Info" message.

There are two possible commands:
* "Add:{animalName}:{dailyFoodLimit}:{area}":
    > Add the animal and its daily food limit to your records.
    It is guaranteed that the names of the animals are unique and there will never be animals with the same name.
    If it already exists, just increase the value of the daily food limit with the current one that is given.

*  "Feed:{animalName}:{food}:{area}":
    > Check if the animal exists and if it does, reduce its daily food limit with the given food for feeding.
    If its limit reaches 0 or less, the animal is considered successfully fed
    and you need to remove it from your records and print the following message:
    "{animalName} was successfully fed"

You need to know the count of hungry animals there are left in each area in the end.
If an animal has daily food limit above 0, it is considered hungry.
In the end, you have to print each animal with its daily food limit
    sorted in descending order by the daily food limit and then by its name in ascending order in the following format:
    Animals:
    {animalName} -> {dailyFoodLimit}g
    {animalName} -> {dailyFoodLimit}g

Afterwards, print the areas with the count of animals, which are not fed in descending order by the count of animals.
If an area has 0 hungry animals in it, don't print it. The output must be in the following format:
    Areas with hungry animals:
    {areaName} : {countOfUnfedAnimals}
    {areaName} : {countOfUnfedAnimals}

'''

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
