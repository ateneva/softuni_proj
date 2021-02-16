
 # **************** 01.lemonade stand (simple calculations) ********************

lemons = float(input())
sugar = float(input())
water = float(input())

juice = lemons * 980
lemonade = juice + (water * 1000) + (sugar * 0.7)
cups = round(lemonade // 150)
earned = cups * 1.20

print(f"All cups sold: {cups}")
print(f"Money earned: {earned:.2f}")
