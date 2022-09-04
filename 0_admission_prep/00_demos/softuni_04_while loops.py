
# numbers in range 1 to 100------------------------------
number = int(input())

while number < 1 or number > 100:
    print("Invalid number!")
    number = int(input())

print(f"The number is: {number}")

# password ---------------------------------------------------------------------
username = input()
password = input()
data = input()

while data != password:
    data = input()
print(f"Welcome {username}!")

# sequence 2k + 1---------------------------------------------------------------
n = int(input())
number = 1

while number <= n:
    print(number)
    number = 2 * number + 1

# max number--------------------------------------------------------------------
import sys

n = int(input())
input_count = 0
max_number = -sys.maxsize

while input_count < n:
    number = int(input())
    input_count +=1

    if number > max_number:
        max_number = number

print(max_number)

# min number--------------------------------------------------------------------
import sys

n = int(input())
input_count = 0
min_number = sys.maxsize

while input_count < n:
    number = int(input())
    input_count +=1

    if number < min_number:
        min_number = number

print(min_number)

# coins (exam problem)----------------------------------------------------------
import math as m

money = float(input())
money *= 100
money = m.floor(money)
counter = 0

while money > 0:
    if money / 200 >= 1:
        counter += 1
        money -= 200
    else:
        if money / 100 >= 1:
            counter += 1
            money -= 100
        else:
            if money / 50 >= 1:
                counter += 1
                money -= 50
            else:
                if money / 20 >= 1:
                    counter += 1
                    money -= 20
                else:
                    if money / 10 >= 1:
                        counter += 1
                        money -= 10
                    else:
                        if money / 5 >= 1:
                            counter += 1
                            money -= 5
                        else:
                            if money / 2 >= 1:
                                counter += 1
                                money -= 2
                            else:
                                if money / 1 >= 1:
                                    counter += 1
                                    money -= 1
print(counter)

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

# darts tournament (exam 27th July 2019)----------------------------------------

initial_score = int(input())
moves = 0

while initial_score > 0:
    score_range = input()
    score = int(input())
    moves += 1

    if score_range == 'bullseye':
        initial_score = 0

    elif score_range == 'number section':
        initial_score -= score

    elif score_range == 'double ring':
        initial_score -= score * 2

    elif score_range == 'triple ring':
        initial_score -= score * 3

    if initial_score == 0\
            and score_range != 'bullseye':
        print(f'Congratulations! You won the game in {moves} moves!')

    elif initial_score == 0 \
            and score_range == 'bullseye':
        print(f'Congratulations! You won the game with a bullseye in {moves} moves!')
        break

if initial_score != 0:
    print(f'Sorry, you lost. Score difference: {abs(0-initial_score)}.')


# moving------------------------------------------------------------------------

width = int(input())
length = int(input())
height = int(input())
boxes = input()
box_volume = 0
isFree = True

while not boxes == 'Done':
    boxes = int(boxes)
    box_volume += boxes

    if box_volume > (width * length * height):
        isFree = False
        break

    boxes = input()  # breaking the endless looping

space_left = abs((width * length * height) - box_volume)
if isFree: # boolean take a value of true by default
    print(f'{space_left} Cubic meters left.')
else:
    print(f'No more free space! You need {space_left} Cubic meters more.')


# cake--------------------------------------------------------------------------
width = int(input())
length = int(input())
cake = input()
slices = 0

while not cake == 'STOP':
    cake = int(cake)
    slices += cake

    if slices > width*length:
        left = abs(slices - width*length)
        print(f'No more cake left! You need {left} pieces more.')
        break
    cake = input()

else:
    left = abs(slices - width*length)
    print(f'{left} pieces are left.')


# exam preparation--------------------------------------------------------------

fail_grades = int(input())
problem = input()
problems = 0
grades = 0
fail_grades_counter = 0
last_problem = 'None'

while not problem == 'Enough':
    grade = int(input())
    grades += grade
    problems += 1
    last_problem = problem

    if grade <= 4:
        fail_grades_counter += 1
        if fail_grades_counter == fail_grades:
            break

    problem = input()

if fail_grades_counter == fail_grades:
    print(f'You need a break, {fail_grades} poor grades.')

else:
    avg_score = grades / problems
    print(f'Average score: %.2f' % avg_score)
    print(f'Number of problems: {problems}')
    print(f'Last problem: {last_problem}')


# -----------------------------------More exercises-----------------------------

# diswasher --------------------------------------------------------------------
bottles = int(input())
detergent = bottles * 750
cutlery = ''
load = 0
used = 0
dishes = 0
pots = 0

while cutlery != 'End':    # until input = "End" or we've run out of detergent
    cutlery = input()
    load += 1

    if cutlery == 'End':
        if used <= detergent:
            print(f'Detergent was enough!')
            print(f'{dishes} dishes and {pots} pots were washed.')
            print(f'Leftover detergent {abs(detergent - used)} ml.')

        else:
            print(f'Not enough detergent, {abs(detergent - used)} ml. more necessary!')
        break

    if load % 3 == 0:
        used += int(cutlery) * 15
        pots += int(cutlery)

    else:
        used += int(cutlery) * 5
        dishes += int(cutlery)

    if used > detergent:
        print(f'Not enough detergent, {abs(detergent - used)} ml. more necessary!')
        break
        # program ends when "End" is passed on as input or when detergent is over

# report system ----------------------------------------------------------------
final_balance = int(input())
sales_price = input()
payment = 0
card = 0
cash = 0
card_sum = 0
cash_sum = 0
total_raised = 0

while not sales_price == 'End':
    sales_price = int(sales_price)
    payment += 1

    if payment % 2 != 0:             # cash payment
        if sales_price > 100:
            print(f'Error in transaction!')
        else:
            print(f'Product sold!')
            cash_sum += sales_price
            cash += 1

    elif payment % 2 == 0:          # card payment
        if sales_price < 10:
            print(f'Error in transaction!')
        else:
            print(f'Product sold!')
            card_sum += sales_price
            card += 1

    total_raised = card_sum + cash_sum

    if total_raised >= final_balance:
        print(f'Average CS: {cash_sum / cash:.2f}')
        print(f'Average CC: {card_sum / card:.2f}')
        break

    sales_price = input()

else:
    print(f'Failed to collect required money for charity.')


# stream of letters ------------------------------------------------------------

letter = input()
output = ''
c_found = False
o_found = False
n_found = False
current_word = ''

while not letter == 'End':
    ascii_char = ord(letter)
    upper_case = ascii_char >= 65 and ascii_char <= 90
    lower_case = ascii_char >= 97 and ascii_char <= 122

    if upper_case or lower_case:

        if letter == 'c' and not c_found:
            c_found = True
            letter = input()
            if c_found and o_found and n_found:
                output += f'{current_word} '
                current_word = ''
                c_found = False
                o_found = False
                n_found = False
            continue   # skip to the following iteration

        if letter == 'o' and not o_found:
            o_found = True
            letter = input()
            if c_found and o_found and n_found:
                output += f'{current_word} '
                current_word = ''
                c_found = False
                o_found = False
                n_found = False
            continue

        if letter == 'n' and not n_found:
            n_found = True
            letter = input()
            if c_found and o_found and n_found:
                output += f'{current_word} '
                current_word = ''
                c_found = False
                o_found = False
                n_found = False
            continue

        current_word += letter

    letter = input()

print(output)


# Mock Exam 2019-10-27 bachelor party (while loops) ****************************
guest_fee = int(input())
people = input()
meal_price = 0
total_meal_price = 0
total_people = 0

while not people == 'The restaurant is full':
        people = int(people)
        if people < 5:
            meal_price += people * 100

        elif people >= 5:
            meal_price += people * 70

        total_people += people
        total_meal_price = meal_price

        people = input()

        #print(meal_price)
        #print(total_meal_price)

left = abs(total_meal_price - guest_fee)
if total_meal_price >= guest_fee:
    print(f'You have {total_people} guests and {left} leva left.')
else:
    print(f'You have {total_people} guests and {total_meal_price} leva income, but no singer.')


# walking ----------------------------------------------------------------------
target = 10000
total_steps = 0

while True:
    steps = input()
    if steps == 'Going home':
        steps = int(input())
        total_steps += steps

        if total_steps >= target:
            print('Goal reached! Good job!')
            break                               # don't forget to break
        else:
            more = abs(total_steps - target)
            print(f'{more} more steps to reach goal.')
            break

    elif steps != 'Going home':
        steps = int(steps)
        total_steps += steps
        if total_steps >= target:
            print('Goal reached! Good job!')
            break

# best plane tickets (exam 27th July 2019)--------------------------------------
import sys
import math as m

min_delay = sys.maxsize
hours = 0
minutes = 0

while True:
    ticket = input()
    if ticket == 'End':
        break
    ticket_price = float(input())
    delay = int(input())

    if delay < min_delay:
        min_delay = delay
        last_ticket = ticket
        last_price = ticket_price * 1.96
        hours = m.floor(delay/60)
        minutes = delay % 60

print(f'Ticket found for flight {last_ticket} costs {last_price:.2f} leva with {hours}h {minutes}m stay')
