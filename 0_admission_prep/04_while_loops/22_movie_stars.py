
 # ************* 04.movie stars (while loop) ***********************************

budget = float(input())
actor = input()               # define string input outside the loop

while not actor == 'ACTION':  # program should end with ACTION or when budget has reached 0

    if len(actor) <= 15:
        salary = float(input())    # define the last intger/float input inside the loop

    else:
        salary = budget * 0.20

    budget -= salary

    if budget <= 0:         # check if budget has been exhausted
        print(f"We need {abs(budget):.2f} leva for our actors.")
        break

    actor = input()         # add string input statement to avoid conversion issues and ensure the loop ends

else:
    print(f"We are left with {budget:.2f} leva.")
