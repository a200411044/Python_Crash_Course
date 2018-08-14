#!//usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Simon Law

# Version 1
'''
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
'''

# Version 2
'''
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)
'''

# Version 3

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)



