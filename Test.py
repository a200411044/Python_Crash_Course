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

#my_age = 19
#print("I'm Simon, and I'm " + str(my_age) + " years old!")

#3-4:
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

#3-8
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

#4-1
#print('For foods:')
#foods = ['ice cream', 'sushi', 'uni', 'cola']

#for foods in foods:
#    print(foods.title())
#    print('My favorite food is ' + foods.title() + '!\n')

#print('I really like these kind of foods!\n')
#print('For pets:')
#pet = ['dog', 'cat', 'owl']

#for pet in pet:
#    print("A " + pet.title() + " would make a great pet!\n")

#print("Any of these animals would make a great pet!")

#4-3 1-20
#for value in range(1,21):
#    print(value)

#4-4 1-100k
'''
for value in range(1,1000001):
    print(value)
'''

#4-5
'''
one_to_10k = range(1,1000001)
print(min(one_to_10k))
print(max(one_to_10k))
print(sum(one_to_10k))
'''

#4-6
'''
odd_numbers = list(range(1,21,2))
print(odd_numbers)
for odd_numbers in odd_numbers:
    print(odd_numbers)

print('And these are the odd numbers in 1-20')
'''

#4-7
'''
multiple_of_3 = list(range(3,31,3))
print(multiple_of_3)
for multiple_of_3 in multiple_of_3:
    print(multiple_of_3)

print('And these are the multiply of 3')
'''

#4-8
'''
squares = []
for value in range(1,11):
    squares.append(value**2)
    print(squares)
'''

#4-9
'''
squares = [value**2 for value in range(1,11)]
print(squares)
'''

