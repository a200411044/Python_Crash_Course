#!//usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Simon Law
age = 12

if age < 4:
    print("You admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print('Your admission cost is $10.')

# Faster_way
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")

