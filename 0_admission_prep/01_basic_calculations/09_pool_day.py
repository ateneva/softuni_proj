
 # **************** 01.pool day (simple calculations) **************************

import math as m

people = int(input())
admission = float(input())
chaizlongue = float(input())
umbrella = float(input())

admissions = admission * people
chaizlongues = m.ceil(people * 0.75) * chaizlongue
umbreallas = m.ceil(people * 0.50) * umbrella

needed = admissions + chaizlongues + umbreallas
print(f"{needed:.2f} lv.")
