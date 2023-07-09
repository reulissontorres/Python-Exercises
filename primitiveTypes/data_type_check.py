# Code that checks the type and additional characteristics of user input.

value = input('Enter something: ')
print('The primitive type of this value is', type(value))
print('Contains only spaces?', value.isspace())
print('Is it a number?', value.isnumeric())
print('Is it alphabetical?', value.isalpha())
print('Is it alphanumeric?', value.isalnum())
print('Is it in uppercase?', value.isupper())
print('Is it in lowercase?', value.islower())
print('Is it capitalized?', value.istitle())
