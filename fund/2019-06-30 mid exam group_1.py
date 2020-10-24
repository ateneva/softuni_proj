
# ************************************************ Group 1 ****************************************************

# ---------------------------------01. Distance Calculator (Conditional Statements)---------------------------

# ------- 100 points -----------------------

steps = int(input())
step_length_cm = float(input())
target_distance_m = int(input())
distance_steps = steps * step_length_cm
distance = 0

for step in range(1, steps + 1):
    if step % 5 == 0:
        distance_steps -= step_length_cm * 0.30

    distance = distance_steps/100           # convert to meters

percentage = distance/target_distance_m * 100
print(f"You travelled {percentage:.2f}% of the distance!")

# ---------------------------------02. Number Array (Lists Basic)---------------------------------------------

# --------------90 points (1x runtime error)-------------------------
numbers = list(map(int, input().split(" ")))
command = input()

while command != "End":
    command = command.split(" ")
    do = command[0]

    #print(numbers, command, do)

    if do == 'Switch':
        idx = int(command[1])
        if 0 <= idx < len(numbers):
            num = numbers[idx]
            numbers[idx] = num * -1

    elif do == 'Change':
        idx = int(command[1])
        value = int(command[2])

        if 0 <= idx < len(numbers):
            num = numbers[idx]
            numbers[idx] = value

    elif do == 'Sum':
        num_type = command[1]
        if num_type == 'Negative':
            negatives = [n for n in numbers if n < 0]
            print(sum(negatives))

        elif num_type == "Positive":
            positives = [p for p in numbers if p >= 0]
            print(sum(positives))

        elif num_type == "All":
            print(sum(numbers))

    positives = [p for p in numbers if p >= 0]

    command = input()
# print(numbers)
print(" ".join(map(str, positives)))

# ---------------------------------03. Contact List (Lists Advanced) -----------------------------------------

# ------------90 points (1 X incorrect answer)--------------------
contacts = input().split(" ")

while True:
    command = input()
    do = command.split(" ")[0]

    if do == "Add":
        contact = command.split(" ")[1]
        idx = int(command.split(" ")[2])
        if contact not in contacts:
            contacts.append(contact)
        else:
            if 0 <= idx <= len(contacts):
                contacts.insert(idx, contact)

    elif do == "Remove":
        idx = int(command.split(" ")[1])
        if 0 <= idx <= len(contacts):
            del contacts[idx]

    elif do == "Export":
        start = int(command.split(" ")[1])
        count = int(command.split(" ")[2])
        if count >= len(contacts):
            export = contacts[start:]
        else:
            export = contacts[start:count]
        print(" ".join(export))

    elif do == "Print":
        print_type = command.split(" ")[1]
        if print_type == "Normal":
            contacts = " ".join(contacts)
            print(f"Contacts: {contacts}")
        else:
            contacts.reverse()
            contacts = " ".join(contacts)
            print(f"Contacts: {contacts}")

        break
