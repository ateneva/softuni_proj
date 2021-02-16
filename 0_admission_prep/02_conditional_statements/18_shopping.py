
 # ********* 02.shopping (conditional statements) ******************************

budget = float(input())
videocard = int(input())
processor = int(input())
RAM = int(input())

videocards = videocard * 250
processors = processor * (videocards * 0.35)
RAMs = RAM * (videocards * 0.10)

cost = videocards + processors + RAMs

if videocard > processor:
    cost = cost * 0.85
else:
    cost = cost

left = abs(budget - cost)

if cost <= budget:
    print(f"You have {left:.2f} leva left!")
else:
    print(f"Not enough money! You need {left:.2f} leva more!")
