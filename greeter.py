#!//usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Simon Law

# Version 1
'''
name = input("Please enter your name: ")
print("Hello, " + name + "!")
'''

# Version 2
'''
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")
'''

# Version 3
def greet_user(username):
    print("Hello, " + username.title() + "!")

greet_user('jesse')
