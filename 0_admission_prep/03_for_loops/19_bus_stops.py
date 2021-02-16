
# Mock Exam 2019-10-27 bus stops ***********************************************

starting_passengers = int(input())
stops = int(input())

for i in range(1, stops + 1):
    off = int(input())
    on = int(input())

    starting_passengers += on
    starting_passengers -= off

    if i % 2 != 0:
        starting_passengers += 2
    else:
        starting_passengers -= 2

print(f'The final number of passengers is : {starting_passengers}')
