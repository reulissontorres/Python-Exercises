'''
This code calculates the total payment for a car rental based on the number of days rented and the kilometers driven. It assumes a daily rate of R$60 and a rate of R$0.15 per kilometer. The total payment amount is displayed as output.
'''

days = int(input('How many days rented? '))
km = float(input('How many kilometers driven? '))
total_payment = (days * 60) + (km * 0.15)
print('The total amount to be paid is R${:.2f}'.format(total_payment))
