
# ------------------------10. Bread Factory (exam problem) ---------------------

'''
As a young baker, you are baking the bread out of the bakery.
You have initial energy 100 and initial coins 100.
You will be given a string, representing the working day events.
Each event is separated with '|' (vertical bar): "event1|event2|event3…"
Each event contains event name or item and a number, separated by dash("{event/ingredient}-{number}"

* If the event is "rest": you gain energy, the number in the second part.

    But your energy cannot exceed your initial energy (100).
        Print: "You gained {0} energy.".

    After that, print your current energy: "Current energy: {0}.".
    * If the event is "order": You've earned some coins, the number in the second part.
        Each time you get an order, your energy decreases with 30 points.

        - If you have energy to complete the order, print: "You earned {0} coins.".
        - If your energy drops below 0, you skip the order and gain 50 energy points.
            Print: "You had to rest!".

*  In any other case you are having an ingredient, you have to buy.
    The second part of the event, contains the coins you have to spent and remove from your coins.
    - If you are not bankrupt (coins <= 0) you've bought the ingredient successfully,
        and you should print ("You bought {ingredient}.")

    - If you went bankrupt, print "Closed! Cannot afford {ingredient}." and your bakery rush is over.

If you managed to handle all events through the day, print on the next three lines:
"Day completed!", "Coins: {coins}", "Energy: {energy}".
'''

energy = 100
coins = 100
events = input().split('|')
completed = True

for event in events:
    activity = event.split('-')[0]
    number = int(event.split('-')[1])

    if activity == 'rest':
        if energy < 100:
            energy += number
            print(f"You gained {number} energy.")
        else:
            print(f"You gained {0} energy.")
        print(f"Current energy: {energy}.")

    elif activity == 'order':
        if (energy - 30) < 0:
            energy += 50
            print("You had to rest!")
        else:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")

    else:
        if (coins - number) > 0:
            print(f"You bought {activity}.")
            coins -= number
        else:
            print(f"Closed! Cannot afford {activity}.")
            completed = False
            break

if completed:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
