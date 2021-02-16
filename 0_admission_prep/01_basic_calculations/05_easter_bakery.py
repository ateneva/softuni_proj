
# *********** 01.Easter Bakery (simple calculations) ***************************

flour_price = float(input())
flour = float(input())
sugar = float(input())
eggs = int(input())
powder = int(input())

sugar_price = flour_price * 0.75

batter = flour * flour_price \
         + sugar * sugar_price \
         + eggs * (flour_price * 1.10) \
         + powder * (sugar_price * 0.20)

print(f'{batter:.2f}')
