
# Problem statement in
# https://github.com/ateneva/softuni_proj/wiki/fund_lists_10.bread_factory

# ------------------------10. Bread Factory (exam problem) -----------------------------------------------------

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
