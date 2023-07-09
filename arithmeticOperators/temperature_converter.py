'''
This code converts a temperature from Celsius (˚C) to Fahrenheit (˚F). It takes the temperature in Celsius as input and calculates the equivalent temperature in Fahrenheit using the conversion formula. The original temperature in Celsius and the converted temperature in Fahrenheit are displayed as output.
'''

celsius = float(input('Enter the temperature in ˚C: '))
fahrenheit = 9 * celsius / 5 + 32
print('The temperature of {}˚C corresponds to {}˚F!'.format(celsius, fahrenheit))
