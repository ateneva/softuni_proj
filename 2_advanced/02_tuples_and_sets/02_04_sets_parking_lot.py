
# ----------------Problem 4: Parking Lot ----------------------------------

'''
Write a program that:
    •	Records a car number for every car that enters the parking lot
    •	Removes a car number when the car leaves the parking lot
The input will be the number of commands, which you will receive, and cars in the format: direction, car_number.
Print the car numbers, which are still in the parking lot.
NOTE: The order in which we print the result does not matter.
'''

num_cars = int(input())
parking = set()

for c in range(1, num_cars + 1):
    car = input().split(", ")       # OR (direction, car_plate) = input().split(", ")
    direction = car[0]
    car_plate = car[1]

    if direction == 'IN':
        parking.add(car_plate)

    elif direction == 'OUT':
        parking.remove(car_plate)

if len(parking) > 0:
    for p in parking:
        print(p)
else:
    print("Parking Lot is Empty")
