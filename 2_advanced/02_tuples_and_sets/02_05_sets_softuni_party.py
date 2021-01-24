
# ------------------------Problem 5: SoftUni Party ------------------------------

'''
There is a party at SoftUni. Many guests are invited and there are two types of them: Regular and VIP.
When a guest comes, check if he/she exists in any of the two reservation lists.

All reservation numbers are 8 characters long and all VIP numbers will start with a digit.
    First, you will be receiving the number of guests and their reservation numbers.
    After that, you will be receiving guests, who came to the party, until you receive the "END" command:
In the end, print the count of the guests who didn't come to the party and their reservation numbers.

The VIP guests must be first.
Both the VIP and the Regular guests must be sorted in ascending order.
'''

# input total number of reservations
def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines

# input guests who arrived
def input_to_list_until_command(end_command):
    lines = []
    while True:
        command = input()
        if command == end_command:
            break
        lines.append(command)

    return lines


# determine if VIP
def is_vip_guest(guest):
    return guest[0].isdigit()


def get_all_guests(guests):
    vip_guests = []
    regular_guests = []
    for guest in guests:
        if is_vip_guest(guest):
            vip_guests.append(guest)
        else:
            regular_guests.append(guest)
    return (sorted(vip_guests), sorted(regular_guests))


def print_result(guests):
    print(len(guests))
    (vip_guests, regular_guests) = get_all_guests(guests)

    for guest in vip_guests:
        print(guest)

    for guest in regular_guests:
        print(guest)


num_guests = int(input())
reservations = input_to_list(num_guests)
guests_arrived = input_to_list_until_command('END')
no_shows = set(reservations).difference(guests_arrived)
print_result(no_shows)
