
# -----------------------------------06. Courses -------------------------------

'''
Write a program that keeps information about courses.
Each course has a name and registered students.

Until you receive the command "end", you will be receiving a course name and a student name
    in the format: "{courseName} : {studentName}".

* Check if such course already exists, and if not, add the course.
* Register the user into the course.

When you receive the command "end", print the courses with their names and total registered users,
    ordered by the count of registered users in descending order.

For each contest print the registered users ordered by name in ascending order.
    "{courseName}: {registeredStudents}"

'''
# --------------100 points --------------------
enrolment = input()
courses = {}                            # if course does not exist, add it -> course must be key

while enrolment != 'end':
    enrolment = enrolment.split(" : ")
    course = enrolment[0]
    student = enrolment[1]

    if course not in courses.keys():    # dictionary key does not exist, create it with element key
        courses[course] = [student]     # there could be multiple students per course --> we create a list
    else:
        courses[course].append(student)

    courses[course].sort()              # sort the list in ascending order
    enrolment = input()

# for key, value in sorted(myDict.items(), key=lambda e: e[1][2])  # sort by key and value
# courses = dict(sorted(courses.items(), key=lambda x: x[0]))  # sort by key

courses = dict(sorted(courses.items(), key=lambda s: (-len(s[1])))) # sort in descending order by value

for course, persons in courses.items():
    print(f'{course}: {len(persons)}')
    for person in persons:
        print(f'-- {person}')
