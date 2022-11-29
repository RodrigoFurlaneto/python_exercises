# This program will raffle some name
from random import choice
first_name = input('Enter the first name: ')
second_name = input('Enter the second name: ')
third_name = input('Enter the third name: ')
fourth_name = input('Enter the fourth name: ')
name_list = [first_name, second_name, third_name, fourth_name]

luck_name = choice(name_list)

print('Congratulations {}!'.format(luck_name.title()))
