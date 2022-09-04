# account balance---------------------------------------------------------------
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

# input
# 3
# 5.51
# 69.42
# 100

# Input
# 5
# 120
# 45.55
# -150

# graduation: part 1------------------------------------------------------------
name = input()
school_year = 1
grades = 0

while school_year <= 12:
    #print(f"year: {school_year}")
    grade = float(input())
    if grade >=4:
        school_year +=1
        grades += grade
        avg_grade = grades/12

print(f'{name} graduated. Average grade: %.2f' % avg_grade)

# Pesho
# 4
# 5.5
# 6
# 5.43
# 4.5
# 6
# 5.55
# 5
# 6
# 6

# Ani
# 5
# 5.32
# 6
# 5.43
# 5
# 6
# 5.5
# 4.55
# 5
# 6

# graduation: part 2------------------------------------------------------------
name = input()
school_year = 1
counter = 0
grades = 0

while school_year <= 12:
    if counter == 2:
        print(f'{name} has been excluded at {school_year} grade')
        break

    grade = float(input())
    if grade < 4.00:
        counter +=1

    else:
        school_year +=1
        grades += grade
        avg_grade = grades/12

if counter < 2:
    print(f'{name} graduated. Average grade: %.2f' % avg_grade)


# old books---------------------------------------------------------------------
fav_book = input()
books = int(input())
iterations = 0
isFound = False

while iterations < books:
    book = input()
    if book == fav_book:
        isFound = True
        break

    iterations +=1
    if iterations == books:
        isFound = False
        break

if isFound:
    print(f'You checked {iterations} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {iterations} books.')

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


# 2000
# 1000
# spend
# 1200
# save
# 2000

# 110
# 60
# spend
# 10
# spend
# 10
# spend
# 10
# spend
# 10
# spend
# 10
