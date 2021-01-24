
# --------------------Problem 2: average grades----------------------------------

'''
Write a program, which reads a name of a student and their grades and adds them to the student record.
Print the  name of the students with their grades and their average grade.
The order in which we print the result does not matter.
'''

students_num = int(input())
students = {}

for s in range(1, students_num + 1):
    student_record = input().split(" ")

    student = student_record[0]
    grade = float(student_record[1])

    if student not in students:
        students[student] = [grade]
    else:
        students[student].append(grade)

for (student, grades) in students.items():                 # access the tuple from the dictionary
    avg_grade = round(sum(grades)/len(grades), 2)
    all_grades = ' '.join(f'{grade:.2f}' for grade in grades)
    print(f'{student} -> {all_grades} (avg: {avg_grade:.2f})')
