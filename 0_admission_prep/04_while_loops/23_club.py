

 # ****************04.club (while loop) ****************************************

target_revenue = float(input())
cocktail = input()                               # define string input outside the loop
revenue = 0
order_revenue = 0

while not cocktail == 'Party!':                  # program should end when input = "Party" or target revenue has been reached

    order = int(input())                         # define the last intger/float input inside the loop
    order_revenue = int(len(cocktail)) * order

    if order_revenue % 2 == 0:
        revenue += order_revenue
    else:
        revenue += order_revenue * 0.75

    if revenue >= target_revenue:                # check if target revenue has been reached
        print(f"Target acquired.")
        print(f"Club income - {revenue:.2f} leva.")
        break

    cocktail = input()                           # add string input statement to avoid conversion issues and ensure the loop ends

else:
    print(f"We need {abs(target_revenue - revenue):.2f} leva more.")
    print(f"Club income - {revenue:.2f} leva.")
