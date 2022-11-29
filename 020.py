# This program will draw a sequence of names
import random
first_name = input('Enter the first name: ')
second_name = input('Enter the second name: ')
third_name = input('Enter the third name: ')
fourth_name = input('Enter the first name: ')
names_list = [first_name, second_name, third_name, fourth_name]
random.shuffle(names_list)
print('The sequence is: {}'.format(names_list))
