

# *********** 04.cinema voucher (while loop) ***********************************

voucher = int(input())
purchase = input()       # define string input outside the loop
tickets = 0
others = 0

# program should end on input = 'End' oe when there's no more money on the voucher
while not purchase == 'End':
    if len(purchase) > 8:
        price = ord(purchase[0]) + ord(purchase[1])
        if price <= voucher:
            tickets += 1
    else:
        price = ord(purchase[0])
        if price <= voucher:
            others += 1

    voucher -= price
    if voucher < 0:        # check for the voucher remaining balance
        break

    purchase = input()     # add string input statement to ensure that the loop ends

print(tickets)
print(others)
