
 # ************* 02.summer shopping (condtiinal statements) ********************

budget = float(input())
towel = float(input())
discount = int(input())

umbrella = (2/3) * towel
flops = umbrella * 0.75
bag = (towel + flops) * 1/3

payable = (towel + umbrella + flops + bag) * (1-discount/100)
left = abs(payable - budget)

if payable <= budget:
    print(f"Annie's sum is {payable:.2f} lv. She has {left:.2f} lv. left.")
else:
    print(f"Annie's sum is {payable:.2f} lv. She needs {left:.2f} lv. more.")
