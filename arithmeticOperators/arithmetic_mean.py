# Calculates the arithmetic mean (average) of two grades and displays the result.

first_grade = float(input('Enter the first grade of the student: '))
second_grade = float(input('Enter the second grade of the student: '))
average = (first_grade + second_grade) / 2
print('The average between {:.1f} and {:.1f} is {:.1f}'.format(first_grade, second_grade, average))
