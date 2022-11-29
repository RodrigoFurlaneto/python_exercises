# This program will calculate the sine, cosine and tangent of an angle
from math import sin, cos, tan, radians
angle = float(input('Enter an angle: '))
rad_angle = radians(angle)
sine = sin(rad_angle)
cosine = cos(rad_angle)
tangent = tan(rad_angle)

print('The sine, cosine and tangent of {:.2f} are respectively: {:.2f}; {:.2f}; {:.2f}'.format(angle, sine, cosine, tangent))
