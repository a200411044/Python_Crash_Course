#!//usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Simon Law
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

# Version 1
'''
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
'''

# Version 2
for k, v in user_0.items():
    print("\nk: " + k)
    print("v: " + v)
