# This application will read a salary and give a 15% boost

salary = float(input('Enter the salary: $'))

new_salary = salary * 1.15

print('Your new salary with a 15% increase is ${:.2f}'.format(new_salary))
