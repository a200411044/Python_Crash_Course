#!//usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Simon Law
'''
requested_topping = ['mushrooms', 'extra cheese']


if requested_topping != 'anchovies':
    print("Hold the anchovies!")
'''

'''
if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")
if 'pepperoni' in requested_topping:  # Must use "if" because elif will skip your command!
    print("Adding pepperoni.")
if 'extra cheese' in requested_topping:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
'''

'''
requested_topping = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_topping:
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")
'''

'''
requested_topping = []

if requested_topping:
    for requested_topping in requested_topping:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
'''

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_toppings in requested_toppings:
    if requested_toppings in available_toppings:
        print("Adding " + requested_toppings + ".")
    else:
        print("Sorry, we don't have " + requested_toppings + ".")

print("\nFinished making your pizza!")




