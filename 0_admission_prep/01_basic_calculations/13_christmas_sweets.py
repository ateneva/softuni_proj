
# ************ 01.christmas sweets (simple operations and calculations) ********

baklava = float(input())
muffins = float(input())
stollen_kg = float(input())
sweets_kg = float(input())
biscuits_kg = float(input())

stollen = (baklava * 1.60) * stollen_kg
sweets = (muffins * 1.80 ) * sweets_kg
biscuits = biscuits_kg * 7.50

total = stollen + sweets + biscuits

print(f'{total:.2f}')
