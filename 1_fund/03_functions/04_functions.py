
# ***************************************** Lab ****************************************************

# 01. grades -----------------------------------------------
grade = float(input())

def grades(grade):
    if grade >= 2.00 and grade <= 2.99:
        return "Fail"

    elif grade >= 3.00 and grade <= 3.49:
        return "Poor"

    elif grade >= 3.50 and grade <= 4.49:
        return 'Good'

    elif grade >= 4.50 and grade <= 5.49:
        return 'Very Good'

    elif grade >= 5.50 and grade <= 6.00:
        return 'Excellent'

# needs to printed with all parameters, else throws an error
print(grades(grade))

# 02. calculations -------------------------------------------

operator = input()
param1 = int(input())
param2 = int(input())

def calc(operator, param1, param2):

    if operator == 'multiply':
        return param1 * param2

    elif operator == 'divide':
        return param1/param2

    elif operator == 'add':
        return param1 + param2

    elif operator == 'subtract':
        return param1 - param2

# needs to printed with all parameters, else throws an error
print(int(calc(operator, param1, param2)))

# 03. repeat string --------------------------------------------

string = input()
repeat = int(input())

def rep(string, repeat):
    return string * repeat

# needs to printed with all parameters, else throws an error
print(rep(string, repeat))

# 04. orders ---------------------------------------------------
product = input()
qty = int(input())

def bill(product, qty):
    if product == 'coffee':
        return qty * 1.50

    elif product == 'water':
        return qty * 1.00

    elif product == 'coke':
        return qty * 1.40

    elif product == 'snacks':
        return qty * 2.00

print(f'{bill(product, qty):.2f}')

# 05. calculate rectangle area ---------------------------------
width = int(input())
height = int(input())

def area(width, height):
    return width * height

print(area(width, height))

# ******************************************* Exercises *****************************************************

# 01. smallest of three numbers -------------------------------------------------
a = int(input())
b = int(input())
c = int(input())

def smallest(a, b, c):
    return min(a, b, c)

print(smallest(a, b, c))

# 02. add and subtract ----------------------------------------------------------
a = int(input())
b = int(input())
c = int(input())

def sum_numbers(a, b):
    return a + b

def subtract(sum_numbers, c):
    return sum_numbers - c

def add_and_subtract(a, b, c):
    sum_numbers(a,b)
    subtract(sum_numbers(a,b,),c)

print(subtract(sum_numbers(a,b,),c))

# 03. characters in range -------------------------------------------------------
char1 = input()
char2 = input()

def chars(char1, char2):
    rng = []
    for char in range(ord(char1) + 1, ord(char2)):
        rng.append(chr(char))

    return ' '.join(rng)

print(chars(char1, char2))

# 04. odd and even sum ----------------------------------------------------------
n = input()

def odd_or_sum(n):
    even = []
    odd = []
    for x in n:
        if int(x) % 2 == 0:
            even.append(int(x))
        elif int(x) % 2 != 0:
            odd.append(int(x))
    even = sum(even)
    odd = sum(odd)

    return [odd, even]

print(f'Odd sum = {odd_or_sum(n)[0]}, Even sum = {odd_or_sum(n)[1]}')

# 05. palindrome integers --------------------------------------------------------
numbers = input()

def palindrome(numbers):
    result = []
    numbers = numbers.split(',')
    for num in numbers:
        num = num.lstrip()
        #print(''.join(list(num)))
        #print(''.join(list(reversed(num))))
        if ''.join(list(num)) == ''.join(list(reversed(num))):
            result.append('True')
        else:
            result.append('False')
    return result

for r in palindrome(numbers):
    print(r)

# 06. password validator ----------------------------------------------------------
password = input()

def validate(password):
    messages = []
    length = len(password)  >= 6 and len(password) <= 10

    # all returns True if all the conditions are met
    letters_and_digits = all([x.isdigit() or x.isalpha() for x in password ])

    # returns True if a character is a letter or num
    l_and_d = password.isalnum()
    num_digits = len([x for x in password if x.isdigit()]) >= 2

    # check validity
    if length and letters_and_digits and num_digits:
        messages.append("Password is valid")

    if not length:
        messages.append("Password must be between 6 and 10 characters")

    if not letters_and_digits:
        messages.append("Password must consist only of letters and digits")

    if not num_digits:
        messages.append("Password must have at least 2 digits")

    return messages

print('\n'.join(validate(password)))  # join on a new line

# 07. perfect number -----------------------------------------------------------------
numb = int(input())

def is_perfect(numb):
    divisors = []
    for i in range(1, numb):
        if numb % i == 0:
            divisors.append(i)
    return sum(divisors) == numb

if is_perfect(numb):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")

# 08. loading bar (exam problem)-------------------------------------------------------
x = int(input())

def progress_bar(x):
    progress = int(x/10) * '%'
    bar = int(10 - (x/10)) * '.'

    if x > 0 and x < 100:
        result = f'{x}% ' + '[' + progress + bar + ']' + '\n' + 'Still loading...'
    else:
        result = '100% Complete!' + '\n' + '[' + progress + bar + ']'

    return result

print(progress_bar(x))

# 09. factorial division (exam problem)--------------------------------------------------
x = int(input())
y = int(input())

def factorial(x,y):
    for i in range(1, x):
        x *= i

    for j in range(1, y):
        y *= j

    return x/y

print(f'{factorial(x,y):.2f}')

# 10. array manipulator (exam problem) --------------------------------------------------
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

# ******************************************* More Exercises ****************************************************