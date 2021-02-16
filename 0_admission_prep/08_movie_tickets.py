
 # ********** 06.movie tickets (nested loop) ***********************************

a1 = int(input())
a2 = int(input())
n = int(input())
ticket = ''

for i in range(a1, a2):
    for j in range(1, n):
        for k in range(1, n//2):
            ticket = chr(i) + '-' + str(j) + str(k) + str(i)

            if i % 2 != 0 \
                 and (i + j + k) % 2 != 0:
                 print(ticket)
