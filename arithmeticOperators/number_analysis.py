'''
Obtains a number from the user and calculates
its predecessor and successor, then displays the results.
'''

number = int(input('Enter a number: '))
predecessor = number - 1
successor = number + 1
print('Analyzing the value {}, its predecessor is {} and the successor is {}'.format(number, predecessor, successor))
