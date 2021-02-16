
# clever Lilly (exam problem)--------------------------------------------

age = int(input())
price_washing_machine = float(input())
toy_price = int(input())
toys = 0
gift_money = 0
gift_sum = 0
given_to_bro = 0

for i in range(1, age+1):
    if i % 2 == 0:
        gift_sum += 10
        gift_money += gift_sum
        given_to_bro += 1

    elif i % 2 != 0:
        toys += 1

sales_income = toys * toy_price
total_money = sales_income + gift_money - given_to_bro

left = abs(total_money - price_washing_machine)
if total_money > price_washing_machine:
    print(f'Yes! %.2f' % left)
else:
    print(f'No! %.2f' % left)
