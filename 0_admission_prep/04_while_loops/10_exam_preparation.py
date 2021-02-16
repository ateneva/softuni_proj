
# exam preparation-------------------------------------------------------------

fail_grades = int(input())
problem = input()
problems = 0
grades = 0
fail_grades_counter = 0
last_problem = 'None'

while not problem == 'Enough':
    grade = int(input())
    grades += grade
    problems += 1
    last_problem = problem

    if grade <= 4:
        fail_grades_counter += 1
        if fail_grades_counter == fail_grades:
            break

    problem = input()

if fail_grades_counter == fail_grades:
    print(f'You need a break, {fail_grades} poor grades.')

else:
    avg_score = grades / problems
    print(f'Average score: %.2f' % avg_score)
    print(f'Number of problems: {problems}')
    print(f'Last problem: {last_problem}')
