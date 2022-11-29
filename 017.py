# This program read calculate the hypotenuse of a right triangle
from math import pow, sqrt

opposite_leg = float(input('Enter the opposite leg: '))
adjacent_leg = float(input('Enter the adjacent leg: '))

hypotenuse = sqrt(pow(opposite_leg, 2) + pow(adjacent_leg, 2))

print('The hypotenuse of this right triangle is {:.2f}'.format(hypotenuse))
