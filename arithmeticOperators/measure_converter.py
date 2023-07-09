'''
This code converts a distance in meters to other units of measurement, such as kilometers, hectometers, decameters, decimeters, centimeters, and millimeters, displaying the results.
'''

distance = float(input('Enter a distance in meters: '))
km = distance / 1000
hm = distance / 100
dam = distance / 10
dm = distance * 10
cm = distance * 100
mm = distance * 1000
print('The measurement of {}m corresponds to:\n{:.3f}km\n{:.2f}hm\n{:.1f}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(distance, km, hm, dam, dm, cm, mm))
