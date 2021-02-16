
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
