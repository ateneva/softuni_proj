
# grades -----------------------------------------------------------------------

students = int(input())
excellent = 0
good = 0
average = 0
poor = 0
all_grades = 0

for student in range(students):
    grade = float(input())
    all_grades += grade

    if grade >= 2.00 and grade <= 2.99:
        poor += 1

    elif grade >= 3.00 and grade <= 3.99:
        average += 1

    elif grade >= 4.00 and grade <=4.99:
        good += 1

    else:
        excellent += 1

print(f'Top students: {excellent/students*100:.2f}%')
print(f'Between 4.00 and 4.99: {good/students*100:.2f}%')
print(f'Between 3.00 and 3.99: {average/students*100:.2f}%')
print(f'Fail: {poor/students*100:.2f}%')
print(f'Average: {all_grades/students:.2f}')
