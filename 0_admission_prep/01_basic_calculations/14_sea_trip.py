
# sea trip (simple calculations) ***********************************************

food_per_day = float(input())
gifts_per_day = float(input())
hotel_per_day = float(input())

distance = 210 * 2
days = 3
petrol_price = 1.85
petrol_needed = distance / 100 * 7

petrol_money = petrol_needed * petrol_price
#print(petrol_money)

hotel_expenses = hotel_per_day * 0.90 \
                 + hotel_per_day * 0.85 \
                 + hotel_per_day * 0.80

#print(hotel_expenses)

total_needed = food_per_day * days \
               + gifts_per_day * days \
               + hotel_expenses \
               + petrol_money

print(f'Money needed: {total_needed:.2f}')
