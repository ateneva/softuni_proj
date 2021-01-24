
# ------------------------08. Seize the Fire (exam problem) --------------------

'''
Create a program that calculates the water that is needed to put out a "fire cell",
    based on the given information about its "fire level" and how much it gets affected by water.

First, you will be given the level of fire inside the cell with the integer value of the cell,
    which represents the needed water to put out the fire.

They will be given in the following format:
"{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}#{typeOfFire} = {valueOfCell}……"

Afterwards you will receive the amount of water you have for putting out the fires.
There is a range of fire for each of the fire types,
    and if a cell’s value is below or exceeds it, it is invalid and you don’t need to put it out.

**Type of Fire -> Range**
* High -> 81 - 125
* Medium -> 51 - 80
* Low -> 1 - 50

If a cell is valid, you have to put it out by reducing the water with its value.
Putting out fire also takes effort and you need to calculate it.
Its value is equal to 25% of the cell’s value.
In the end you will have to print the total effort.
Keep putting out cells until you run out of water.
If you don’t have enough water to put out a given cell – skip it and try the next one.
In the end, print the cells you have put out in the following format:
    "Cells:
    - {cell1}
    - {cell2}
    - {cell3}
    ……
    - {cellN}"
    "Effort: {effort}"
In the end, print the total fire you have put out from all of the cells in the following format:
    "Total Fire: {totalFire}"

'''

fires = input().split('#')
well = int(input())
effort = 0
cells = []

#print(fires)

for fire in fires:
    fire_type = fire.split('=')[0].strip()
    water = int(fire.split('=')[1])
    #print(fire_type, water)

    if well >= water:
        if fire_type == 'High':
            if water >= 81 and water <= 125:
                well -= water
                effort += water * 0.25
                cells.append(water)

        elif fire_type == 'Medium':
            if water >= 51 and water <= 80:
                well -= water
                effort += water * 0.25
                cells.append(water)

        elif fire_type == 'Low':
            if water >= 1 and water <= 50:
                well -= water
                effort += water * 0.25
                cells.append(water)

#print(cells)
print(f'Cells:')
for cell in cells:
    print(f'- {cell}')

print(f"Effort: {effort:.2f}")
print(f'Total Fire: {sum(cells)}')
