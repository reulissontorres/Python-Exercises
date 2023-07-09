'''
This code calculates the area of a wall based on its width and height. It then determines the amount of paint needed to paint the wall, assuming a paint coverage of 2 square meters per liter. The dimensions of the wall and the required amount of paint are displayed as output.
'''

width = float(input('Width of the wall: '))
height = float(input('Height of the wall: '))
area = width * height
print('Your wall has dimensions {}x{} and its area is {}m².'.format(width, height, area))
paint = area / 2
print('To paint this wall, you will need {} liters of paint.'.format(paint))
