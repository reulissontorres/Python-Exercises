'''
This code calculates the new salary of an employee after a 15% raise. It takes the current salary as input and applies the raise to calculate the new salary. The original salary and the new salary are displayed as output.
'''

salary = float(input('What is the employee\'s salary? R$'))
new_salary = salary + (salary * 15 / 100)
print('An employee who earned R${:.2f}, with a 15% raise, now earns R${:.2f}'.format(salary, new_salary))
