
# ********** 01.Easter Lunch (simple calculations) *****************************

bakery = int(input())
eggs = int(input())
cookies = int(input())

bakery_cost = bakery * 3.20
eggs_cost = eggs * 4.35
cookies_cost = cookies * 5.40
paint_cost = eggs * 12 * 0.15

total = bakery_cost + eggs_cost + cookies_cost + paint_cost

print(f'{total:.2f}')
