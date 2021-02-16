
# fishing --------------------------------------------------------------------------

quota = int(input())
fish_caught = 0
balance = 0
stop = False

for fish in range(quota):
    fish_name = input()
    if fish_name == 'Stop':
        stop = True
        break

    fish_weight = float(input())
    fish_caught += 1

    fish_value = 0
    for value in fish_name:
        money = ord(value)
        fish_value += money

    fish_value /= fish_weight

    if fish_caught % 3 == 0:
        balance += fish_value
    else:
        balance -= fish_value

if not stop:
    print(f'Lyubo fulfilled the quota!')

if balance >= 0:
    print(f"Lyubo's profit from {fish_caught} fishes is {balance:.2f} leva.")
else:
    print(f"Lyubo lost {abs(balance):.2f} leva today.")
