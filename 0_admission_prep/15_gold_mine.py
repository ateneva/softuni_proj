
# gold mine (nested mine) ------------------------------------------------------

locations = int(input())
total_retrieved = 0
avg_retrieved = 0
days_mined = 0
stop = False

for location in range(1, locations + 1):
    expected = float(input())
    days = int(input())

    for day in range(1, days + 1):
        retrieved = float(input())
        total_retrieved += retrieved

        avg_retrieved = total_retrieved/days

    if avg_retrieved >= expected:
        print(f"Good job! Average gold per day: {avg_retrieved:.2f}.")
    else:
        print(f"You need {abs(avg_retrieved - expected):.2f} gold.")

    total_retrieved = 0
    avg_retrieved = total_retrieved / days
