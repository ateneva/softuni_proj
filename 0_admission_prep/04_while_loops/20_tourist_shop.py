
# *************** 04. toursit shiop (while loop) *******************************

budget = float(input())
product = input()            # define string input outside the loop
orders = 0
total_price = 0

# program should end with ACTION or when price is greater than remaining budget
while not product == 'Stop':
    price = float(input())   # define the last intger/float input inside the loop
    orders += 1

    if orders % 3 == 0:
        price /= 2
    else:
        price

    budget -= price
    total_price += price

    if (budget - price) <= 0:                  # check if budget has been exhausted
        print(f"You don't have enough money!")
        print(f"You need {abs(budget):.2f} leva!")
        break

    product = input()    # add string input statement to avoid conversion issues and ensure the loop ends

else:
    print(f"You bought {orders} products for {total_price:.2f} leva.")
