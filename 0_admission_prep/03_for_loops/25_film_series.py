
# Admission exam 2019-06-16 Series *********************************************

budget = float(input())
film_series = int(input())
total_price = 0

for film in range(film_series):
    series_title = input()
    series_price = float(input())

    if series_title == 'Thrones':
        series_price *= 0.50

    elif series_title == 'Lucifer':
        series_price *= 0.60

    elif series_title == 'Protector':
        series_price *= 0.70

    elif series_title == 'TotalDrama':
        series_price *= 0.80

    elif series_title == 'Area':
        series_price *= 0.90

    total_price += series_price

left = abs(budget - total_price)

if total_price <= budget:
    print(f"You bought all the series and left with {left:.2f} lv.")
else:
    print(f"You need {left:.2f} lv. more to buy the series!")
