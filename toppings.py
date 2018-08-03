#!//usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Simon Law
requested_topping = ['mushrooms', 'extra cheese']

'''
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
'''

if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")
if 'pepperoni' in requested_topping:  # Must use "if" because elif will skip your command!
    print("Adding pepperoni.")
if 'extra cheese' in requested_topping:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")


