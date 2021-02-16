
 # ************** 01.repainting (simple calculations) **************************

naylone = int(input())
paint = int(input())
dilution = int(input())
labour = int(input())

naylone_cost = (naylone + 2) * 1.50
paint_cost = (paint + paint*0.10) * 14.50
dilution_cost = dilution * 5.00

labour_cost = (naylone_cost + paint_cost + dilution_cost + 0.40) * 0.30
labour_cost = labour_cost * labour

total_cost = (naylone_cost + paint_cost + dilution_cost + 0.40) + labour_cost

print(f"Total expenses: {total_cost:.2f} lv.")
