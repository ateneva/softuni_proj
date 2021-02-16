
# back to the past -----------------------------------------

inheritance = float(input())
year = int(input())
age = 17
total_expenses = 0

for y in range(1800, year+1):
    age += 1
    if y % 2 == 0:
        expenses = 12000
    else:
        expenses = 12000 + 50 * age

    # print(age)
    # print(expenses)
    # print(total_expenses)
    total_expenses += expenses
    inheritance -= expenses
    # print(inheritance)

if inheritance >= 0:
    print(f'Yes! He will live a carefree life and will have {abs(inheritance):.2f} dollars left.')
else:
    print(f'He will need {abs(inheritance):.2f} dollars to survive.')
