
# ********** 01.tennis equipment (simple calculations) *************************
import math as m

tennis_racket = float(input())
count_rackets = int(input())
count_trainers = int(input())

trainers = tennis_racket * (1/6)
total_rackets = count_rackets * tennis_racket
total_trainers = count_trainers * trainers
misc = (total_rackets + total_trainers) * 0.20

total = total_rackets\
        + total_trainers \
        + misc

self = m.floor(1/8 * total)
sponsors = m.ceil(7/8 * total)

print(f"Price to be paid by Djokovic {self}")
print(f"Price to be paid by sponsors {sponsors}")
