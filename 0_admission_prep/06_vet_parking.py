
# ************** 06.vet parking (nested loop) **********************************

days = int(input())
hours = int(input())
fee = 0
total_fees = 0

for d in range(1, days + 1):
    day_total = 0

    for h in range(1, hours + 1):
        if d % 2 == 0 and h % 2 != 0:
            fee = 2.50
        elif d % 2 != 0 and h % 2 == 0:
            fee = 1.25
        else:
            fee = 1.00

        day_total += fee

    print(f"Day: {d} - {day_total:.2f} leva")

    total_fees += day_total

print(f"Total: {total_fees:.2f} leva")
