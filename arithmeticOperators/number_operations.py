'''
Calculates the double, triple, and square root of a given number,
and displays the results.
'''

number = int(input('Enter a number: '))
double = number * 2
triple = number * 3
square_root = pow(number, 1/2)
print('The double of {} is {}.'.format(number, double))
print('The triple of {} is {}.\nThe square root of {} is {:.2f}.'.format(number, triple, number, square_root))
