
# travelling--------------------------------------------------------------------
destination = input()

while destination != 'End':
    budget = float(input())
    savings = 0
    has_given_up = False

    while savings < budget:
        current_input = input()
        if current_input == 'End':
            has_given_up = True
            break
        current_savings = float(current_input)
        savings += current_savings

    if has_given_up:
        break

    print(f'Going to {destination}!')
    destination = input()


# cinema tickets (exam problem)-------------------------------------------------
movie = input()
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while movie != 'Finish':
    seats = int(input())
    seats_taken = 0
    while seats_taken < seats:
        ticket = input()

        if ticket == 'End':
            break
        seats_taken += 1

        if ticket == 'student':
            student_tickets += 1

        elif ticket == 'standard':
            standard_tickets += 1

        elif ticket == 'kid':
            kid_tickets += 1

    capacity = seats_taken / seats * 100
    print(f'{movie} - {capacity :.2f}% full.')
    movie = input()

tickets = student_tickets + standard_tickets + kid_tickets
print(f'Total tickets: {tickets}')
print(f'{student_tickets / tickets * 100 :.2f}% student tickets.')
print(f'{standard_tickets / tickets * 100 :.2f}% standard tickets.')
print(f'{kid_tickets / tickets * 100 :.2f}% kids tickets.')
