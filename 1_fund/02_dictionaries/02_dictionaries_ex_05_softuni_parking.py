
# ---------------------------05. SoftUni Parking -------------------------------

'''
Write a program, which validates a parking place for an online service.
Users can register to park and unregister to leave.

The program receives 2 types of commands:
*  "register {username} {licensePlateNumber}":
    > The system only supports one car per user at the moment,
        so if a user tries to register another license plate, using the same username,
        the system should print: "ERROR: already registered with plate number {licensePlateNumber}"

* If the aforementioned checks passes successfully, the plate can be registered,
    so the system should print: "{username} registered {licensePlateNumber} successfully"

* "unregister {username}":
    > If the user is not present in the database, the system should print: "ERROR: user {username} not found"
    > If the aforementioned check passes successfully, the system should print: "{username} unregistered successfully"

After you execute all of the commands, print all the currently registered users and their license plates in the format:
* "{username} => {licensePlateNumber}"
'''

# --------------100 points --------------------

def print_dict(dictionary, template):
    for (key, value) in dictionary.items():
        print(template.format(key, value))

parking_log = {}
parkings = int(input())

for parking in range(1, parkings + 1):
    transaction = input().split(" ")

    action = transaction[0]
    username = transaction[1]

    if action == 'register':
        platenumber = transaction[2]

        if username not in parking_log:        # populate the dictionary first
            parking_log[username] = platenumber
            print(f"{username} registered {platenumber} successfully")
        else:
            print(f"ERROR: already registered with plate number {platenumber}")

    else:
        if username not in parking_log:
            print(f"ERROR: user {username} not found")
        else:
            parking_log.pop(username)
            print(f"{username} unregistered successfully")

print_dict(parking_log, '{} => {}')
