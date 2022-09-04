# 08. Mutate Strings (exam problem) ------------------------
first = input()
second = input()
prv = first

for idx in range(0, len(first)):
    new = ''
    for i in range(0, idx + 1):
        new += second[i]

    for j in range(idx + 1, len(first)):
        new += first[j]

    if new != prv:
        print(new)
        prv = new
