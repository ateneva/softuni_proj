
# ********** 06.christmas decoration (nested loop) *****************************

budget = int(input())
decoration = input()
money_left = 0
cost = 0

while decoration != 'Stop':
    for char in decoration:
        i = ord(char)
        cost += i

    if cost <= budget:
        print("Item successfully purchased!")
    else:
        print("Not enough money!")
        break

    money_left = abs(budget-cost)
    decoration = input()

else:
    print(f"Money left: {money_left}")
