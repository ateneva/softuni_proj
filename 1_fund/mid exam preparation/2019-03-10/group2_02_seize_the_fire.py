
# ********************************************** Group 2 *********************************************************

# ---------------------------------02. Seize the Fire (Lists Basic)-----------------------------------------------
# https://github.com/ateneva/softuni_proj/wiki/fund_20190310_mid_exam_group_2

# ------- 100 points -----------------------

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
