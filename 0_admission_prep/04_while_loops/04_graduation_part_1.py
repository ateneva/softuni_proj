
# graduation: part 1------------------------------------------------------------
name = input()
school_year = 1
grades = 0

while school_year <= 12:
    #print(f"year: {school_year}")
    grade = float(input())
    if grade >=4:
        school_year +=1
        grades += grade
        avg_grade = grades/12

print(f'{name} graduated. Average grade: %.2f' % avg_grade)
