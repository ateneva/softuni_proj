
# trip to the world cup (simple calculations)--------------------------------------------------
outbound_ticket = float(input())
inbound_ticket = float(input())
game_price = float(input())
games = int(input())
discount = int(input())

flight_tickets = 6 * (inbound_ticket + outbound_ticket)
discount_value = flight_tickets * (discount/100)

flight_tickets -= discount_value
game_tickets = 6 * games * game_price

total_sum = flight_tickets + game_tickets
per_person = total_sum / 6

print(f'Total sum: {total_sum:.2f} lv.')
print(f'Each friend has to pay {per_person:.2f} lv.')

# maiden party (conditional statements)----------------------------------------------------------

maiden_party_cost = float(input())
love_messages = int(input())
roses = int(input())
keyrings = int(input())
drawings = int(input())
charms = int(input())

goods = love_messages + roses + keyrings + drawings + charms
revenue = (love_messages * 0.60) \
            + (roses * 7.2) \
            + (keyrings * 3.6) \
            + (drawings * 18.20) \
            + (charms * 22) \

if goods >= 25:
    revenue = revenue * (1-0.35)
else:
    revenue

after_hosting = revenue * 0.90
left = abs(after_hosting - maiden_party_cost)

if after_hosting >= maiden_party_cost:
    print(f'Yes! {left:.2f} lv left.')
else:
    print(f'Not enough money! {left:.2f} lv needed.')

# game statistics (nested conditionals)--------------------------------------------------------

minutes = int(input())
player = input()

if minutes == 0:
    print(f'Match has just began!')

elif minutes > 0 and minutes < 45:
    print(f'First half time.')

    if minutes >= 1 and minutes <= 10:
        print(f'{player} missed a penalty.')
        if minutes % 2 == 0:
            print(f'{player} was injured after the penalty.')

    elif minutes > 10 and minutes <= 35:
        print(f'{player} received yellow card.')
        if minutes % 2 != 0:
            print(f'{player} got another yellow card.')

    elif minutes > 35 and minutes < 45:
        print(f'{player} SCORED A GOAL !!!')

elif minutes >= 45:
    print(f'Second half time.')

    if minutes > 45 and minutes <= 55:
        print(f'{player} got a freekick.')
        if minutes % 2 == 0:
            print(f'{player} missed the freekick.')

    elif minutes > 55 and minutes <= 80:
        print(f'{player} missed a shot from corner.')
        if minutes % 2 != 0:
            print(f'{player} has been changed with another player.')

    elif minutes > 80 and minutes <= 90:
        print(f'{player} SCORED A GOAL FROM PENALTY !!!')

# coffee shop (while loop)-------------------------------------------------------------------------------


# game  (for loops)--------------------------------------------------------------------------------------

team = input()
games = int(input())

total_played = 0
avg_duration = 0
with_penalties = 0  # > 120
prolonged = 0       # > 90

for game in range(games):
    minutes = int(input())

    if minutes > 120:
        with_penalties += 1
        total_played += minutes

    elif minutes > 90 and minutes <= 120:
        prolonged += 1
        total_played += minutes

    else:
        total_played += minutes

    avg_duration = total_played/games

print(f"{team} has played {total_played} minutes. Average minutes per game: {avg_duration:.2f}")
print(f"Games with penalties: {with_penalties}")
print(f"Games with additional time: {prolonged}")

# gold mine (nested mine) -------------------------------------------------------------------------------------

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



