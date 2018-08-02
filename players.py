#!//usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Simon Law

players = ['simon', 'peter', 'tom', 'amy', 'tim']
'''
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
'''
print("Here are the first three players on my team:")
for players in players[:3]:
    print(players.title())