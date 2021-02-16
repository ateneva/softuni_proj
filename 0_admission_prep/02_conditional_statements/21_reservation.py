
 # *********** 02.reservaton (conditional statements) **************************

book_date = int(input())
book_month = int(input())
arrival_date = int(input())
arrival_month = int(input())
departure_date = int(input())
departure_month = int(input())

nights = departure_date - arrival_date

if book_month < arrival_month:
    price = 25
    payable = nights * price * 0.80

elif (arrival_date - book_date) >= 10:
    price = 25
    payable = nights * price

else:
    price = 30
    payable = nights * price

print(f"Your stay from {arrival_date}/{arrival_month} to {departure_date}/{departure_month} will cost {payable:.2f}")
