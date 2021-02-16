
# ************ 01.basketball equipment (simple calculations) *******************

training = int(input())

shoes = training * 0.60
sportswear = shoes * 0.80
ball = sportswear * 0.25
misc = ball * 0.20

total = training + shoes + sportswear + ball + misc
print(f'{total:.2f}')
