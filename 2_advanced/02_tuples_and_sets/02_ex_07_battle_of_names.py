
# --------------------problem 7: battle of names-------------------------------

'''
You will receive a number N. On the next N lines, you will be receiving names.
You must sum the ascii values of each letter in the name and integer divide it
by the value of the current line. Save the devised number to a set of either odd
 or even numbers, depending if it's an odd or even number.

After that, sum the values of the odd and even numbers.
    - If the summed numbers are equal, print the union values, separated by ", ".
    - If the odd sum is bigger than the even, print the different values, separated by ", ".
    - If the even sum is bigger than the odd, print the symmetric different values, separated by ", ".

'''

names = int(input())
odd = set()
even = set()

for i in range(1, names + 1):
    devised = 0    # must be reset for every name
    name = input()
    devised = sum([ord(n) for n in name]) // i

    if devised % 2 == 0:
        even.add(devised)
    else:
        odd.add(devised)

#print(odd, even)
#print(sum(odd), sum(even))

if sum(odd) > sum(even):
    print(", ".join([str(j) for j in (odd - even)]))

elif sum(even) > sum(odd):
    print(", ".join([str(k) for k in (odd ^ even)]))

else:
    print(", ".join([str(l) for l in (odd | even)]))
