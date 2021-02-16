
# trip to the world cup (simple calculations)-----------------------------------
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
