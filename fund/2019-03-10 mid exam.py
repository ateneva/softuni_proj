
# ************************************************ Group 1 ****************************************************

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

# ********************************************** Group 2 *********************************************************

# ---------------------------------01. The Hunting Games (Conditional Statements)---------------------------------

# ------- 100 points -----------------------

days = int(input())
players = int(input())
energy = float(input())
water_pp_pd = float(input())   # pre-calculate rations per person, per day outside the loop
food_pp_pd = float(input())    # pre-calculate rations per person, per day outside the loop

water = water_pp_pd * players * days
food = food_pp_pd * players * days
energy_left = True

for day in range(1, days + 1):
    energy_loss = float(input())
    energy -= energy_loss

    if energy <= 0:            # needs to be the first stement as energy can fall below 0 before replenishment
        energy_left = False
        break

    if day % 2 == 0:
        energy += energy * 0.05
        water -= water * 0.30

    if day % 3 == 0:
        energy += energy * 0.10
        food -= food / players

if energy_left:
    print(f"You are ready for the quest. You will be left with - {energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {food:.2f} food and {water:.2f} water.")
    

# ---------------------------------02. Seize the Fire (Lists Basic)-----------------------------------------------

# ------- 100 points -----------------------

fires = input().split('#')
well = int(input())
effort = 0
cells = []

#print(fires)

for fire in fires:
    fire_type = fire.split('=')[0].strip()
    water = int(fire.split('=')[1])
    #print(fire_type, water)

    if well >= water:
        if fire_type == 'High':
            if water >= 81 and water <= 125:
                well -= water
                effort += water * 0.25
                cells.append(water)

        elif fire_type == 'Medium':
            if water >= 51 and water <= 80:
                well -= water
                effort += water * 0.25
                cells.append(water)

        elif fire_type == 'Low':
            if water >= 1 and water <= 50:
                well -= water
                effort += water * 0.25
                cells.append(water)

#print(cells)
print(f'Cells:')
for cell in cells:
    print(f'- {cell}')

print(f"Effort: {effort:.2f}")
print(f'Total Fire: {sum(cells)}')

# ---------------------------------03. The Final Quest (Lists Advanced)---------------------------------------------

# ------- 83 points /2 x incorrect answer/-----------

message = input().split(" ")
instructions = input()

while instructions != 'Stop':
    instructions = instructions.split(" ")
    command = instructions[0]

    if command == 'Delete':
        delete_idx = int(instructions[1]) + 1
        if delete_idx < len(message):
            del message[delete_idx]

    elif command == 'Swap':             # if swap or replace, just use the indexing
        word_one = instructions[1]
        word_two = instructions[2]

        if word_one in message:
            if word_two in message:
                idx_one = int(message.index(word_one)) # save the position where the  word was
                idx_two = int(message.index(word_two)) # save the position where the word was

                # message.remove(word_one)
                # message.insert(idx_one, word_two)
                # message.remove(word_two)
                # message.insert(idx_two, word_one)
                message[idx_one], message[idx_two] = message[idx_two], message[idx_one]

    elif command == 'Put':
        word = instructions[1]
        position = int(instructions[2])

        if position < len(message):
            message.insert(position-1, word)

    elif command == 'Sort':
        message = sorted(message, reverse=True)   # function --> can be applied on any iterable
        message.sort(reverse=True)                # method  --> only applicable to lists

    elif command == 'Replace':
        word_one = instructions[1]
        word_two = instructions[2]

        if word_two in message:
            idx = message.index(word_two) # save the position
            message.remove(word_two)
            message.insert(idx, word_one)

    #print(message, instructions, command)

    instructions = input()

print(" " .join(message))