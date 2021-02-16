

# maiden party (conditional statements)-----------------------------------------

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
