
 # ******************* 01.savings (simple calculations) ************************

income = float(input())
months = int(input())
expenses = float(input())

unforeseen = income * 0.30

savings = income - (expenses + unforeseen)
total_savings = months * savings
percent = savings / income * 100

print(f"She can save {percent:.2f}%")
print(f"{total_savings:.2f}")
