
# multiplication table *********************************************************
number = int(input())

start = int(str(number)[-1:])
mid = int(str(number)[-2])
end = int(str(number)[:1])

for i in range(1, start+1):
    for j in range(1, mid+1):
        for k in range(1, end+1):
            print(f'{i} * {j} * {k} = {i * j * k};')
