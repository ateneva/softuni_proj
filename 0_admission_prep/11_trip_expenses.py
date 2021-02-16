
 # ******************06.trip expenses (nested loop) ****************************

vacation = int(input())
left = 0

for day in range(1, vacation + 1):
    price = input()
    budget = 60
    budget = budget + left
    products = 0

    while not price == 'Day over':
        price = int(price)
        budget -= price
        products += 1

        if budget <= 0:
            left = 0
            print(f"Daily limit exceeded! You've bought {products} products.")
            break

        if budget > 0:
            left = budget

        price = input()

    else:
        left = budget
        print(f"Money left from today: {budget:.2f}. You've bought {products} products.")
