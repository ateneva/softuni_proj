
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
