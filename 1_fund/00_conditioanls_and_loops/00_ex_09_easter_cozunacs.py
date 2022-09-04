# -------------09. Easter Kozunacs (exam problem)-------------------------------

budget = float(input())
price_flour = float(input())

price_eggs = price_flour * 0.75
price_milk = (price_flour * 1.25) * 0.25

price_kozunak = price_flour + price_eggs + price_milk
kozunaci = 0
eggs = 0

while budget > price_kozunak:
    budget -= price_kozunak
    kozunaci += 1
    eggs += 3

    if kozunaci % 3 == 0:
        eggs -= kozunaci - 2

print(f"You made {kozunaci} cozonacs! Now you have {eggs} eggs and {budget:.2f}BGN left.")
