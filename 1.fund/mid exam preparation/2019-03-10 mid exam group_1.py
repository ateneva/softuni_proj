
# ************************************************ Group 1 ****************************************************
# https://github.com/ateneva/softuni_proj/wiki/fund_20190310_mid_exam_group_1

# ---------------------------------01. Spring Vacation Trip (Conditional Statements)---------------------------

# ------- 100 points -----------------------

days = int(input())
budget = float(input())
people = int(input())
fuel_per_km = float(input())
food_pp = float(input())         # pre-calculate rations per person, per day outside the loop
room_pp = float(input())         # pre-calculate rations per person, per day outside the loop
expenses = 0
depleted_budget = False

if people > 10:
    hotel_expenses = days * people * room_pp * 0.75
else:
    hotel_expenses = days * people * room_pp

food_expenses = days * people * food_pp
expenses = food_expenses + hotel_expenses

for d in range(1, days + 1):
    travelled = float(input())
    travel_expenses = travelled * fuel_per_km

    expenses += travel_expenses

    if d % 3 == 0 or d % 5 == 0:
        expenses += (expenses * 0.40)

    if d % 7 == 0:
        expenses -= (expenses/people)

    if expenses > budget:
        depleted_budget = True
        break

if depleted_budget:
    print(f"Not enough money to continue the trip. You need {abs(expenses-budget):.2f}$ more.")
else:
    print(f"You have reached the destination. You have {abs(expenses-budget):.2f}$ budget left.")


# ---------------------------------02. Hello France (Lists Basic)----------------------------------------------

# ------- 100 points -----------------------

items = input().split('|')
budget = float(input())
max_price = 0
earned = 0
spent = 0
bought = []

for item in items:
    clothing = item.split('->')[0]
    initial_price = float(item.split('->')[1])
    #print(clothing, initial_price)

    if clothing == 'Clothes':
        max_price = 50

    elif clothing == 'Shoes':
        max_price = 35

    elif clothing == 'Accessories':
        max_price = 20.50

    if budget >= initial_price:
        if initial_price <= max_price:
            bought.append(initial_price)
            budget -= initial_price
            spent += initial_price

for price in bought:
    price *= 1.40
    print(f'{price:.2f}', end=' ')
    earned += price

print()
print(f'Profit: {earned-spent:.2f}')

if (earned + budget) >= 150:
    print("Hello, France!")
else:
    print("Time to go.")

# ---------------------------------03. Last Stop (Lists Advanced) -------------------------------------------

# ------- 100 points --------------------------

paintings = list(map(int, input().split(" ")))
instructions = input()

while instructions != "END":
    instructions = instructions.split(" ")
    command = instructions[0]
    if command != "Reverse":
        painting = int(instructions[-1])
    else:
        painting = instructions[-1]

    #print(paintings, command)

    if command == 'Change':
        painting_num = int(instructions[1])
        if painting_num in paintings:
            idx = paintings.index(painting_num)
            paintings.remove(painting_num)
            paintings.insert(idx, painting)

    elif command == "Hide":
        if painting in paintings:
            paintings.remove(painting)

    elif command == "Switch":
        painting_one = int(instructions[1])

        if painting_one in paintings:
            pos_one = paintings.index(painting_one)
            if painting in paintings:
                pos_two = paintings.index(painting)

                paintings[pos_one], paintings [pos_two] = paintings [pos_two], paintings[pos_one]

    elif command == "Insert":
        place = int(instructions[1])
        if place < len(paintings):
            paintings.insert(place + 1, painting)
        else:
            pass

    elif command == "Reverse":
        paintings.reverse()

    #print(paintings, instructions, command, painting)

    instructions = input()

output = " ".join(map(str, paintings))
print(output)
