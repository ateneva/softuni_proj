
# ******************01.oscars ceremony (simple calculations) *******************

hall_rent = int(input())

statues = hall_rent * 0.70
catering = statues * 0.85
sounding = catering * 0.50

total = hall_rent + statues + catering + sounding

print(f'{total:.2f}')
