
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
