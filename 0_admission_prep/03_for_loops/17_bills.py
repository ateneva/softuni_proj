
# bills -----------------------------------------------------------------------

periods = int(input())
water = 0
internet = 0
electricity = 0
other = 0

for period in range(periods):
    electricity_bill = float(input())

    electricity += electricity_bill
    water += 20
    internet += 15
    misc = (electricity_bill + 20 + 15) * 1.20

    other += misc
    total = electricity + water + internet + other

print(f'Electricity: {electricity:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f'Average: {total/periods:.2f} lv')
