
# vacation ---------------------------------------------------------------------
savings = float(input())
balance = float(input())
counter_spend = 0
counter_save = 0
total_days = 0

while balance >= 0:
    activity = input()
    money = float(input())
    total_days += 1

    if activity == 'spend':
        counter_spend += 1
        balance -= money
        if balance < 0:
            balance = 0

        if counter_spend == 5:
            print("You can't save the money.")
            print(f'{total_days}')
            break

    elif activity == 'save':
        counter_spend = 0    # spend counter needs restarting
        counter_save += 1
        balance += money

        if balance >= savings:
            print(f"You saved the money for {total_days} days.")
            break
