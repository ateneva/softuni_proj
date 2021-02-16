
 # ************** 04.cinema (while loop) ***************************************

hall_size = int(input())
cinema_goers = input()   # all string input is defined outside the loop and then converted to integer
capacity = hall_size
total_cinema_goers = 0
total_revenue = 0

 # program should end on input 'Movie time!' or when the hall has reached capacity
while not cinema_goers == 'Movie time!':                #
    cinema_goers = int(cinema_goers)
    capacity -= cinema_goers

    if cinema_goers % 3 == 0:
        revenue = (cinema_goers * 5) - 5
    else:
        revenue = cinema_goers * 5

    total_cinema_goers += cinema_goers
    total_revenue += revenue

    if capacity < 0:                 # check if the hall has reached capacity
        print(f"The cinema is full.")
        print(f"Cinema income - {total_revenue-revenue} lv.")
        break

    cinema_goers = input()  # add string input statement to avoid conversion issues and ensure the loop ends

else:
    print(f"There are {capacity} seats left in the cinema.")
    print(f"Cinema income - {total_revenue} lv.")
