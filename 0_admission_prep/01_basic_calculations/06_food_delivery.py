
# ***********01.food delivery (simple calculations) ****************************

chicken_menus = int(input())
fish_menus = int(input())
veggie_menus = int(input())

chicken = chicken_menus * 10.35
fish = fish_menus * 12.40
veggie = veggie_menus * 8.15

dessert = (chicken + fish + veggie) * 0.20
total = chicken + fish + veggie + dessert + 2.50

print(f"Total: {total:.2f}")
