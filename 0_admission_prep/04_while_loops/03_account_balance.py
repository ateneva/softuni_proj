
# -----------------------account balance----------------------------------------
number_deposits = int(input())
iterations = 0
balance = 0

while iterations < number_deposits:
    deposit = float(input())
    if deposit < 0:
        print("Invalid operation!")
        break

    else:
        balance += deposit
        iterations += 1
        print(f'Increase: %.2f' % deposit)
print(f'Total: %.2f' % balance)
