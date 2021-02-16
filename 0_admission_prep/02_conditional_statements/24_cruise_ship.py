

 # ************03.cruise ship (nested condtiional statements) ******************

cruise = input()
cabin = input()
nights = int(input())
people = 4
price = 0

if cruise == 'Mediterranean':
    if cabin == 'standard cabin':
        price = 27.50

    elif cabin == 'cabin with balcony':
        price = 30.20

    elif cabin == 'apartment':
        price = 40.50

elif cruise == 'Adriatic':
    if cabin == 'standard cabin':
        price = 22.99

    elif cabin == 'cabin with balcony':
        price = 25.00

    elif cabin == 'apartment':
        price = 34.99

elif cruise == 'Aegean':
    if cabin == 'standard cabin':
        price = 23.00

    elif cabin == 'cabin with balcony':
        price = 26.60

    elif cabin == 'apartment':
        price = 39.80

if nights > 7:
    cost = nights * price * people * 0.75
else:
    cost = nights * price * people

print(f"Annie's holiday in the {cruise} sea costs {cost:.2f} lv.")
