
 # ********** 03.luggage tax (nested condtional statements) ********************

height = int(input())
width = int(input())
length = int(input())
ticket = input()
tax = 0

size = height * width * length

if ticket == 'true':
    if size >= 50 and size <= 100:
        tax = 0

    elif size > 100 and size <= 200:
        tax = 10

    elif size > 200 and size <= 300:
        tax = 20

elif ticket == 'false':
    if size >= 50 and size <= 100:
        tax = 25

    elif size > 100 and size <= 200:
        tax = 50

    elif size > 200 and size <= 300:
        tax = 100

print(f"Luggage tax: {tax:.2f}")
