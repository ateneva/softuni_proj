
# graduation: part 2------------------------------------------------------------
name = input()
school_year = 1
counter = 0
grades = 0

while school_year <= 12:
    if counter == 2:
        print(f'{name} has been excluded at {school_year} grade')
        break

    grade = float(input())
    if grade < 4.00:
        counter +=1

    else:
        school_year +=1
        grades += grade
        avg_grade = grades/12

if counter < 2:
    print(f'{name} graduated. Average grade: %.2f' % avg_grade)
