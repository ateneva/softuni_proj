
'''
First you will be given a sequence of integers representing males.
Afterwards you will be given another sequence of integers representing females.
You have to start from the first female and try to match it with the last male.
 - If their values are equal, you have to match them and remove both of them.
    Otherwise you should remove only the female and decrease the value of the male by 2.

 - If someone’s value is equal to or below 0, you should remove him/her from the
    records before trying to match him/her with anybody.

 - Special case - if someone’s value divisible by 25 without remainder, you
    should remove him/her and the next person of the same gender.
You need to stop matching people when you have no more females or males.
'''

from collections import deque

males = [int(i) for i in input().split(' ')]
females = deque([int(i) for i in input().split(' ')])
matches = 0

while females:
    if len(males) > 0:
        female = females[0]
        male = males[-1]

        if female <= 0:
            females.popleft()

        elif male <= 0:
            males.pop()

        # special case
        elif female % 25 == 0:
            for _ in range(0, 1):
                females.popleft()

        elif male % 25 == 0:
            for _ in range(0, 1):
                males.pop()

        elif female == male:
            matches += 1
            females.popleft()
            males.pop()
        else:
            females.popleft()
            males[-1] -= 2

    else:
        break

# print(males)
# print(females)

print(f"Matches: {matches}")

if len(males) == 0:
    print("Males left: none")
else:
    print(f"Males left: {', '.join([str(m) for m in males][::-1])}")

if len(females) == 0:
    print("Females left: none")
else:
    print(f"Females left: {', '.join([str(f) for f in females])}")
