#name = "Simon"
#msg = ["Welcome " + name + " back to our website!"]
#print(msg)

#name2 = "simon law"
#print(name2.lower())
#print(name2.upper())
#print(name2.title())

#famous_people = "Albert Einstein"
#his_qoute = '"A person who never made a mistake tried anything new."'
#famous_qoute = famous_people + ' once said, ' + his_qoute
#print(famous_qoute)

#print(5+3)
#print(10-2)
#print(4*2)
#print(16/2)

# my_age = 19
#print("I'm Simon, and I'm " + str(my_age) + " years old!")

# 3-4:
#invite_list = ['steve jobs', 'bill gates', 'apink', 'g-friend']
#print("I world like to invite " + invite_list[0].title() + " to have dinner with me!")
#print("I world like to invite " + invite_list[1].title() + " to have dinner with me!")
#print("I world like to invite " + invite_list[2].title() + " to have dinner with me!")
#print("I world like to invite " + invite_list[3].title() + " to have dinner with me!")
#too_busy = invite_list.pop(0)
#print(too_busy.title() + " is too busy, so he cannot come to have dinner with me...")
#print("I world like to invite " + invite_list[0].title() + " to have dinner with me!")
#print("I world like to invite " + invite_list[1].title() + " to have dinner with me!")
#print("I world like to invite " + invite_list[2].title() + " to have dinner with me!")

#print("I have found a bigger place to have fun with y'all, so i would like to invite more people to come!")
#invite_list.insert(0, 'bebe rexha')
#invite_list.insert(2, 'zedd')
#invite_list.append('becky g')

#print("I world like to invite " + invite_list[0].title() + " to have dinner with me!")
#print("I world like to invite " + invite_list[1].title() + " to have dinner with me!")
#print("I world like to invite " + invite_list[2].title() + " to have dinner with me!")
#print("I world like to invite " + invite_list[3].title() + " to have dinner with me!")
#print("I world like to invite " + invite_list[4].title() + " to have dinner with me!")
#print("I world like to invite " + invite_list[5].title() + " to have dinner with me!")

#how_many = str(len(invite_list))
#print('I have invited ' + how_many + ' awesome people to come to my dinner!')

#print("Oh shit, now I can only invite two person to have dinner with me, so I will remove some of you from the list now sadly...")
#print("hahaha, " + invite_list.pop().title() + " you are removed from the list, fuck off! lol")
#print("hahaha, " + invite_list.pop().title() + " you are removed from the list, fuck off! lol")
#print("hahaha, " + invite_list.pop().title() + " you are removed from the list, fuck off! lol")
#print("hahaha, " + invite_list.pop().title() + " you are removed from the list, fuck off! lol")
#print("Congrats " + invite_list[0].title() + ", you are still on the fucking list, yolo!!!!!!!!!!!!!!!!")
#print("Congrats " + invite_list[1].title() + ", you are still on the fucking list, yolo!!!!!!!!!!!!!!!!")
#del invite_list[0]
#del invite_list[0]


#print(invite_list)

# 3-8
#travel_list = ['osaka', 'kyoto', 'paris', 'new yorks', 'canada']
#print('Original list:')
#print(travel_list)

#print('\nAlphabetical:')
#print(sorted(travel_list))

#print("\nOriginal list:")
#print(travel_list)

#print('\nReversed Alphabetical:')
#print(sorted(travel_list, reverse=True))

#print('\nReversed list:')
#travel_list.reverse()
#print(travel_list)

#print('\nOriginal list:')
#travel_list.reverse()
#rint(travel_list)

#print('\nAlphabetical:')
#travel_list.sort()
#print(travel_list)

#print('\nReversed Alphabetical:')
#travel_list.sort(reverse=True)
#print(travel_list)

# 4-1
#print('For foods:')
#foods = ['ice cream', 'sushi', 'uni', 'cola']

#for foods in foods:
#    print(foods.title())
#    print('My favorite food is ' + foods.title() + '!\n')

#print('I really like these kind of foods!\n')

# 4-2
#print('For pets:')
#pet = ['dog', 'cat', 'owl']

#for pet in pet:
#    print("A " + pet.title() + " would make a great pet!\n")

#print("Any of these animals would make a great pet!")

# 4-3 1-20
#for value in range(1,21):
#    print(value)

# 4-4 1-100k
'''
for value in range(1,1000001):
    print(value)
'''

# 4-5
'''
one_to_10k = range(1,1000001)
print(min(one_to_10k))
print(max(one_to_10k))
print(sum(one_to_10k))
'''

# 4-6
'''
odd_numbers = list(range(1,21,2))
print(odd_numbers)
for odd_numbers in odd_numbers:
    print(odd_numbers)

print('And these are the odd numbers in 1-20')
'''

# 4-7
'''
multiple_of_3 = list(range(3,31,3))
print(multiple_of_3)
for multiple_of_3 in multiple_of_3:
    print(multiple_of_3)

print('And these are the multiply of 3')
'''

# 4-8
'''
squares = []
for value in range(1,11):
    squares.append(value**2)
    print(squares)
'''

# 4-9
'''
squares = [value**2 for value in range(1,11)]
print(squares)
'''

# 4-10
'''
players = ['simon', 'peter', 'tom', 'amy', 'tim']

print('The first three items in the list are:')
print(players[0:3])

print('\nThree items from the middle of the list are:')
print(players[2:5])

print('\nThe last three items in the list are:')
print(players[2:])
'''

# 4-11
'''
print('For foods:\n')
foods = ['ice cream', 'sushi', 'uni', 'cake']
friend_foods = foods[:]

foods.append('pie')
friend_foods.append('falafel')

for foods in foods:
    print('My favorite foods are:')
    print(foods.title())

print('\n')

for friend_foods in friend_foods:
    print("My friend's favorite foods are:")
    print(friend_foods.title())

print('I really like these kind of foods!\n')
'''

# 4-12
'''
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods:")
for my_foods in my_foods:
    print(my_foods.title())

print("\nMy friend's favorite foods:")

for friend_foods in friend_foods:
    print(friend_foods.title())
'''

# 4-13
'''
buffet_food_list = ['cake', 'steak', 'ice cream', 'oyster', 'sea food']
print("Original Food list:")
for buffet_food_list in buffet_food_list:
    print(buffet_food_list.title())
    #buffet_food_list[3] = 'candy'

buffet_food_list = ['cake', 'pork', 'candy', 'oyster', 'sea food']
print("\nNew food list:")
for buffet_food_list in buffet_food_list:
    print(buffet_food_list.title())
'''

# 5-1
'''
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi', '\n')


print(car == 'bmw', '\n')
print(car == 'benz', '\n')
print(car == 'subaru', '\n')
print(car == 'fuck', '\n')
print(car == 'gtr', '\n')
print(car == 'tesla', '\n')
print(car == 'truck', '\n')
print(car == 'honda', '\n')
print(car == 'toyota', '\n')
print(car == 'subaru', '\n')
'''

# 5-2
'''
name = ['simon', 'tom']
print(name[0] == 'simon')
print(name[1] != 'Tom')
print(name[1].lower() == 'tom')
age = 18
print(age == 18)
print(age != 19)
print(age >= 10)
print(age <= 20)

age_0 = 18
age_1 = 21

print(age_0 >= 10 and age_1 <= 22 )
print(age_0 >= 10 or age_1 <= 20)

users = ['simon', 'tom', 'mary', 'amy']
print('\nIs user Simon on the users list?')
print('simon' in users)
print('\nIs user Tommy on the users list?')
print('tommy' in users)
'''

# 5-3
'''
# Version 1
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print("You have gained 5 points!")

# Version 2
alien_color = ['green', 'yellow', 'red']
if 'blue' in alien_color:
    print("You have gained 5 points!")
'''

# 5-4
'''
# Version 1
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print('You have gained 5 points!\n')
if 'black' in alien_color:
    print('You have gained 10 points!\n')

# Version 2
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print('You have gained 5 points!\n')
else:
    print("You have gained 10 points!\n")
'''

# 5-5
# Version 1
'''
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print("You have gained 5 points!\n")
elif 'yellow' in alien_color:
    print("You have gained 10 points!\n")
else:
    print("You have gained 15 points!\n")

# Version 2
alien_color = ['green', 'yellow', 'red']
if 'black' in alien_color:
    print("You have gained 5 points!\n")
elif 'yellow' in alien_color:
    print("You have gained 10 points!\n")
else:
    print("You have gained 15 points!\n")

# Version 3
alien_color = ['green', 'yellow', 'red']
if 'black' in alien_color:
    print("You have gained 5 points!\n")
elif 'blue' in alien_color:
    print("You have gained 10 points!\n")
else:
    print("You have gained 15 points!\n")
'''

# 5-6
age = 5
if age < 2:
    print("You are baby!")
elif age < 4:
    print("You are learning to walk!")
elif age < 13:
    print("You are child!")
elif age < 20:
    print("You are teenager!")
elif age < 65:
    print("You are adult!")
else:
    print("You are elderly!")
