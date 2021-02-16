

 # *********** 03.travel agency (nested condtiinal statements) *****************

city = input()
package = input()
VIP = input()
days = int(input())
price = 0
discount = 0

if city not in ('Bansko','Borovets','Varna', 'Burgas'):
    print("Invalid input!")

elif package not in ('withEquipment', 'noEquipment', 'withBreakfast', 'noBreakfast'):
    print("Invalid input!")

elif days <= 0:
    print("Days must be positive number!")

elif days > 0:
    if city == 'Bansko' or city == 'Borovets':
        if package == 'withEquipment':
            price = 100
            discount = 0.10
        elif package == 'noEquipment':
            price = 80
            discount = 0.05

    elif city == 'Varna' or city == 'Burgas':
        if package == 'withBreakfast':
            price = 130
            discount = 0.12
        elif package == 'noBreakfast':
            price = 100
            discount = 0.07

    if days > 7:
        days = days - 1

    if VIP == 'yes':
        total_price = days * price * (1-discount)
    else:
        total_price = days * price

    print(f"The price is {total_price:.2f}lv! Have a nice time!")
