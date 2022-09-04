# 10. array manipulator (exam problem) -----------------------------------------
integers = input()
transformation = input()

elements = integers.split(' ')  # forms a list of strings
elements = list(map(int, elements))  # forms a list of integers

transform = transformation.split(' ')[0]

def exchange(idx):  # function does not have printable output just list transformations
    global elements
    if idx < 0 or idx >= len(elements):
        print ("Invalid index")
    else:
        elements = elements[idx+1:] + elements[:idx+1]
        #print(elements)

def max_even_odd(transform):
    global elements
    odds = [i for i in elements if i % 2 == 1]
    evens = [i for i in elements if i % 2 == 0]

    if transform == 'even':
        if len(evens) == 0: # prevents attempts on empty arrays if no evens
            print("No matches")
            return # stores the output and exits the function
        mx_num = evens[0]
    else:
        if len(odds) == 0: # prevents attempts on empty arrays if no odds
            print("No matches")
            return # stores the output and exits the function
        mx_num = odds[0]

    mx_idx = 0

    for i in range(len(elements)):
        curr = elements[i]
        if transform == 'even':
            if curr >= mx_num and curr in evens:
                mx_num = curr
                mx_idx = i
        else:
            if curr >= mx_num and curr in odds:
                mx_num = curr
                mx_idx = i
    print(mx_idx)


# return the min even or odd
def min_even_odd(transform):
    global elements

    global elements
    odds = [i for i in elements if i % 2 == 1]
    evens = [i for i in elements if i % 2 == 0]

    if transform == 'even':
        if len(evens) == 0:  # prevents attempts on empty arrays if no evens
            print("No matches")
            return  # stores the output and exits the function
        mn_num = evens[0]
    else:
        if len(odds) == 0:  # prevents attempts on empty arrays if no odds
            print("No matches")
            return  # stores the output and exits the function
        mn_num = odds[0]

    mn_idx = 0

    for i in range(len(elements)):
        curr = elements[i]
        if transform == 'even':
            if curr <= mn_num and curr in evens:
                mn_num = curr
                mn_idx = i
        else:
            if curr <= mn_num and curr in odds:
                mn_num = curr
                mn_idx = i
    print(mn_idx)

def first_even_odd(count, transform):
    global elements
    result = []

    if count > len(elements):
        print("Invalid count")
        return

    for e in elements:
        if len(result) == count:
            break
        if transform == 'even':
            if e % 2 == 0:
                result.append(e)
        else:
            if e % 2 == 1:
                result.append(e)
    print(result)


def last_even_odd(count, transform):
    global elements
    result = []

    if count > len(elements):
        print("Invalid count")
        return

    reversed_e = list(reversed(elements))
    for e in reversed_e:
        if len(result) == count:
            break
        if transform == 'even':
            if e % 2 == 0:
                result.append(e)
        else:
            if e % 2 == 1:
                result.append(e)
    print(list(reversed(result)))

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# start looping through commands
while transformation != 'end':
    details = transformation.split()

    if details[0] == 'exchange':
        idx = int(details[1])
        exchange(idx)             # call exchange function

    elif details[0] == 'max':
        max_even_odd(details[1])  # call max_even_odd function

    elif details[0] == 'min':
        min_even_odd(details[1])

    elif details[0] == 'first':
        count = int(details[1])
        first_even_odd(count, details[2])

    elif details[0] == 'last':
        count = int(details[1])
        last_even_odd(count, details[2])

    transformation = input()

print(elements)
