
# ********* 02.godzilla vs. kong (conditional statements) **********************

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
