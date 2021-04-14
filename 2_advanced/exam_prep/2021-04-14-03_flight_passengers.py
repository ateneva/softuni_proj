
'''
Create a function named flights that receives a different number of arguments
representing the information about the flights for a day:
    - the destination of each flight
    - the count of passengers that are boarding the plane
    - a string "Finish"

You need to take each argument and make a dictionary with the plane’s
    destination as a key and the passengers as a value of the corresponding key.

If there are more than one flight to the same destination, you should count all
    the passengers that flew to the destination.

You should modify the dictionary until the current argument is equal to "Finish".
'''

def flights(*args):
    schedule = {}
    inputs = list(args)

    for a in inputs:
        if a != 'Finish':
            current_idx = inputs.index(a)

            if len(str(a)) > 3:
                destination = a
                passengers = inputs[current_idx + 1]
                if destination not in schedule:
                    schedule[destination] = passengers
                else:
                    schedule[destination] += passengers
                del inputs[current_idx]
        else:
            break
    return schedule

print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
