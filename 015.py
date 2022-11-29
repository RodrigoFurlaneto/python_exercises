# The user will enter the number of km and how many days he had the car
# the program will say how much he must pay

days = int(input('How many days rented? '))
km = float(input('How many km driven? '))
amount = days * 60 + km * 0.15

print('You must pay ${:.2f}'.format(amount))
