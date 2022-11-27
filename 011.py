# This application will read a height and width of a wall
# and calculate the amount of paint needed (one liter = 2m²)
height = float(input('Enter wall height: '))
width = float(input('Enter wall width: '))

amount_of_paint = height * width / 2

print('You will need {:.2f} liters of paint'.format(amount_of_paint))
