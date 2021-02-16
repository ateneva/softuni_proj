
# ********* 02.football results (conditional statements) ***********************

first_match = input()
second_match = input()
third_match = input()
wins = 0
drawn = 0
losses = 0

if first_match[0] > first_match[2]:
    wins += 1
elif first_match[0] == first_match[2]:
    drawn += 1
else:
    losses += 1

if second_match[0] > second_match[2]:
    wins += 1

elif second_match[0] == second_match[2]:
    drawn += 1
else:
    losses += 1

if third_match[0] > third_match[2]:
    wins += 1

elif third_match[0] == third_match[2]:
    drawn += 1
else:
    losses += 1

print(f"Team won {wins} games.")
print(f"Team lost {losses} games.")
print(f"Drawn games: {drawn}")
