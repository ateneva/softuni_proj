

# Admission Exam 2019-07-28 seats **********************************************

tickets = int(input())

for ticket in range(tickets):
    ticket_num = input()

    if len(ticket_num) >= 5:
        decoded_ticket = ticket_num[0] + str(ord(ticket_num[1]))

    elif ord(ticket_num[0]) >=65 and ord(ticket_num[0]) <= 90:
        decoded_ticket = ticket_num[0] + ticket_num[1] + ticket_num[2]

    else:
        decoded_ticket = ticket_num[3] + ticket_num[1] + ticket_num[2]

    print(f'Seat decoded: {decoded_ticket}')
