#!//usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Simon Law
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

game_active = True
can_edit = False