
# ------------------------------07. Student Academy ----------------------------

'''
Write a program that keeps information about students and their grades.
You will receive n pair of rows.
First you will receive the student's name, after that you will receive his grade.
Check if the student already exists and if not, add him. Keep track of all grades for each student.

When you finish reading the data, keep the students with average grade higher than or equal to 4.50.
Order the filtered students by average grade in descending order.

Print the students and their average grade in the following format:
    {name} –> {averageGrade}
    Format the average grade to the 2nd decimal place.
'''

# --------------100 points --------------------
def print_dict(dictionary, template):
    for (key, value) in dictionary.items():
        print(template.format(key, value))

student_num = int(input())
students = {}
avg_grades = {}

for s in range(student_num):
    student = input()
    grade = float(input())

    if student not in students.keys():  # create a dictionary key if it does not exist
        students[student] = [grade]     # there will be multiple grades per student, so we create a list
    else:
        students[student].append(grade)

# with loop
for k, v in students.items():
    #print(k, v)
    avg_grade = sum(v)/len(v)
    avg_grades[k] = avg_grade
    if avg_grades[k] < 4.50:
        avg_grades.pop(k)

# with comprehension
avg_grades = {k: sum(v)/len(v) for k, v in students.items() if sum(v)/len(v) >= 4.50 }

avg_grades = dict(sorted(avg_grades.items(), key=lambda a: (-a[1]))) # sort descending by grade

print_dict(avg_grades, '{} -> {:.2f}')
