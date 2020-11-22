
# ******************************************** 01.oscars ceremony (simple calculations) *******************************************************************

hall_rent = int(input())

statues = hall_rent * 0.70
catering = statues * 0.85
sounding = catering * 0.50

total = hall_rent + statues + catering + sounding

print(f'{total:.2f}')

# ******************************************** 02.godzilla vs. kong (conditional statements) **************************************************************

budget = float(input())
cast = int(input())
costume = float(input())

decor = budget * 0.10
# print(decor)

if cast >= 150:
    costume = (costume * cast) - (costume * cast * 0.10)
    # print(costume)

else:
    costume = costume * cast
    # print(costume)

expenses = decor + costume
# print(expenses)

if expenses > budget:
    left = abs(budget-expenses)
    print('Not enough money!')
    print('Wingard needs %.2f leva more.' % left)

elif expenses <= budget:
    left = abs(budget-expenses)
    print('Action!')
    print('Wingard starts filming with %.2f leva left.' % left)

# ******************************************** 03.oscars week in cinema (nested condtiinal statements) ****************************************************

movie = input()
hall = input()
tickets = int(input())
price = 0

if hall == 'normal':
    if movie == 'A Star Is Born':
        price = 7.50

    elif movie == 'Bohemian Rhapsody':
        price = 7.35

    elif movie == 'Green Book':
        price = 8.15

    elif movie == 'The Favourite':
        price = 8.75

elif hall == 'luxury':
    if movie == 'A Star Is Born':
        price = 10.50

    elif movie == 'Bohemian Rhapsody':
        price = 9.45

    elif movie == 'Green Book':
        price = 10.25

    elif movie == 'The Favourite':
        price = 11.55

elif hall == 'ultra luxury':
    if movie == 'A Star Is Born':
        price = 13.50

    elif movie == 'Bohemian Rhapsody':
        price = 12.75

    elif movie == 'Green Book':
        price = 13.25

    elif movie == 'The Favourite':
        price = 13.95

revenue = tickets * price
print(f"{movie} -> {revenue:.2f} lv.")

# ******************************************** 04.cinema voucher (while loop) *****************************************************************************

voucher = int(input())
purchase = input()                                # define string input outside the loop
tickets = 0 
others = 0

while not purchase == 'End':                      # program should end on input = 'End' oe when there's no more money on the voucher
    if len(purchase) > 8:
        price = ord(purchase[0]) + ord(purchase[1])
        if price <= voucher:
            tickets += 1
    else:
        price = ord(purchase[0])
        if price <= voucher:
            others += 1

    voucher -= price
    if voucher < 0:                               # check for the voucher remaining balance
        break

    purchase = input()                            # add string input statement to ensure that the loop ends

print(tickets)
print(others)

# ******************************************** 05.movie rating (for loop) *********************************************************************************

movies = int(input())
max_rating = 1
min_rating = 10
total_rating = 0
highest = ''
lowest = ''

for movie in range(movies):
    movie_title = input()
    rating = float(input())
    total_rating += rating

    if rating > max_rating:
        max_rating = rating
        highest = movie_title

    if rating < min_rating:
        min_rating = rating
        lowest = movie_title

    avg_rating = total_rating / movies

print(f"{highest} is with highest rating: {max_rating:.1f}")
print(f"{lowest} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {avg_rating:.1f}")

# ******************************************** 06.cinema tickets (nested loop) *****************************************************************************

movie = input()
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while movie != 'Finish':
    seats = int(input())
    seats_taken = 0
    while seats_taken < seats:
        ticket = input()

        if ticket == 'End':
            break
        seats_taken += 1

        if ticket == 'student':
            student_tickets += 1

        elif ticket == 'standard':
            standard_tickets += 1

        elif ticket == 'kid':
            kid_tickets += 1

    capacity = seats_taken / seats * 100
    print(f'{movie} - {capacity :.2f}% full.')
    movie = input()

tickets = student_tickets + standard_tickets + kid_tickets
print(f'Total tickets: {tickets}')
print(f'{student_tickets / tickets * 100 :.2f}% student tickets.')
print(f'{standard_tickets / tickets * 100 :.2f}% standard tickets.')
print(f'{kid_tickets / tickets * 100 :.2f}% kids tickets.')