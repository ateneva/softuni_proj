

# *********** 03.mobile operator (nested condtiinal statements) ****************

contract_length = input()
contract_type = input()
data_plan = input()
months = int(input())
monthly_fee = 0

if contract_length == 'one':
    if contract_type == 'Small':
        monthly_fee = 9.98

    elif contract_type == 'Middle':
        monthly_fee = 18.99

    elif contract_type == 'Large':
        monthly_fee = 25.98

    elif contract_type == 'ExtraLarge':
        monthly_fee = 35.99

elif contract_length == 'two':
    if contract_type == 'Small':
        monthly_fee = 8.58

    elif contract_type == 'Middle':
        monthly_fee = 17.09

    elif contract_type == 'Large':
        monthly_fee = 23.59

    elif contract_type == 'ExtraLarge':
        monthly_fee = 31.79


if data_plan == 'yes':
    if monthly_fee <= 10.00:
        monthly_fee += 5.50

    elif monthly_fee > 10 and monthly_fee <= 30:
        monthly_fee += 4.35

    elif monthly_fee > 30:
        monthly_fee += 3.85

total = months * monthly_fee

if contract_length == 'two':
    total -= (total * 3.75/100)

print(f"{total:.2f} lv.")
