
# ****************06.Easter Decoration (nested loop) ***************************

customers = int(input())
total = 0

for customer in range(1, customers + 1):
    purchase = input()
    purchases = 0
    spent = 0

    while not purchase == 'Finish':
        purchases += 1

        if purchase == 'basket':
            spent += 1.50
        elif purchase == 'wreath':
            spent += 3.80
        elif purchase == 'chocolate bunny':
            spent += 7.00

        purchase = input()

    else:
        if purchases % 2 == 0:
            spent *= 0.80
        print(f"You purchased {purchases} items for {spent:.2f} leva.")

    total += spent
print(f"Average bill per client is: {total/customers:.2f} leva.")
