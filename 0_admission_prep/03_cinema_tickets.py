
# ******* 06.cinema tickets (nested loop) **************************************

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
