
# ----------------------------Problem 01. grades -------------------------------

'''
Write a function that receives a grade between 2.00 and 6.00
    and prints the corresponding grade in words
     2.00 – 2.99 - "Fail"
     3.00 – 3.49 - "Poor"
     3.50 – 4.49 - "Good"
     4.50 – 5.49 - "Very Good"
     5.50 – 6.00 - "Excellent"
'''

# --------------100 points --------------------
grade = float(input())

def grades(grade):
    if grade >= 2.00 and grade <= 2.99:
        return "Fail"

    elif grade >= 3.00 and grade <= 3.49:
        return "Poor"

    elif grade >= 3.50 and grade <= 4.49:
        return 'Good'

    elif grade >= 4.50 and grade <= 5.49:
        return 'Very Good'

    elif grade >= 5.50 and grade <= 6.00:
        return 'Excellent'

print(grades(grade))
