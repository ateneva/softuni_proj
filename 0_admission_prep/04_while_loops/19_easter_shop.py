

# ************* 04.Easter Shop (while loop) ************************************

initial_volume = int(input())
activity = input()                             # define string input outside the loop
eggs_sold = 0

while not activity == 'Close':                 # program should end on input "Close" or when there are not enough eggs to sell
    eggs = int(input())                        # define the last intger/float input inside the loop

    if activity == 'Buy':
        eggs_sold += eggs
        left = initial_volume
        initial_volume -= eggs

        if initial_volume < 0:                 # check if there are enough eggs to sell
            print("Not enough eggs in store!")
            print(f"You can buy only {left}.")
            break

    if activity == 'Fill':
        initial_volume += eggs

    activity = input()                         # add string input statement to avoid conversion issues and ensure the loop ends

else:
    print("Store is closed!")
    print(f"{eggs_sold} eggs sold.")
