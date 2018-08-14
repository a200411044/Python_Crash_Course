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
'''
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
'''

# 5-7
'''
favorite_fruits = ['apple', 'banana', 'watermelon']
if 'apple' in favorite_fruits:
    print('You really like apple!\n')
if 'banana' in favorite_fruits:
    print('You really like banana!\n')
if 'watermelon' in favorite_fruits:
    print('You really like watermelon!\n')
if 'orange' in favorite_fruits:
    print('You really like orange!')
if 'mango' in favorite_fruits:
    print('You really like mango!')
'''

# 5-8
'''
user = ['simon', 'amy', 'tom', 'alice', 'admin']
for user in user:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user.title() + ", thank you for logging in again")
'''

# 5-9
'''
user = []
if user:
    for user in user:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + user.title() + ", thank you for logging in again")
else:
    print("We need to find more users!")
'''

# 5-10***
'''
current_users = ['SIMON', 'amy', 'tom', 'alice', 'admin']
new_users = ['Simon', 'Amy', 'jack', 'tommy', 'motherfucker']

current_users_lower = [user.lower() for user in current_users]


for new_users in new_users:
    if new_users.lower() in current_users_lower:
        print("User " + new_users + " already exist!")
    else:
        print("User name is available!")
'''

# 5-11
'''
value = range(1,10)
for value in value:
    if value == 1:
        print('1st')
    elif value == 2:
        print('2nd')
    elif value == 3:
        print('3rd')
    else:
        print(str(value) + 'th')
'''

# 6-1
'''
me = {'first_name': 'simon',
      'last_name': 'law',
      'age': 19,
      'city': 'hk'}
print(me)
'''

# 6-2
'''
favorite_number = {'tom': 1,
                   'amy': 2,
                   'simon': 3,
                   'mary': 4,
                   'jack': 5}

num = favorite_number['tom']
print("Tom's favorite number is " + str(num))
num = favorite_number['amy']
print("Amy's favorite number is " + str(num))
num = favorite_number['simon']
print("Simon's favorite number is " + str(num))
num = favorite_number['mary']
print("Mary's favorite number is " + str(num))
num = favorite_number['jack']
print("Jack's favorite number is " + str(num))

'''

# 6-3
'''
python_language = {'print': "Print the statements",
                   'if': 'If the statement is valid, run the command.',
                   'elif': 'If the above statement is invalid, check this statement'
                           ', if valid, run the command.',
                   'else': "If all the above statement is invalid, run "
                           "the command",
                   'xxx = {}': 'Create a dictionary'}

word = 'print'
print("\n" + word.title() + ': ' + python_language['print'])
word = 'if'
print("\n" + word.title() + ': ' + python_language['if'])
word = 'elif'
print("\n" + word.title() + ': ' + python_language['elif'])
word = 'else'
print("\n" + word.title() + ': ' + python_language['else'])
word = 'xxx = {}'
print("\n" + word.title() + ': ' + python_language['xxx = {}'])
'''

# 6-4
'''
python_glossary = {'print': "Print the statements",
                   'if': 'If the statement is valid, run the command.',
                   'elif': 'If the above statement is invalid, check this statement'
                           ', if valid, run the command.',
                   'else': "If all the above statement is invalid, run "
                           "the command",
                   'xxx = {}': 'Create a dictionary',
                   'list.append': 'Add something into list',
                   'name.title()': 'name format',
                   'name.upper': 'format name to upper',
                   'name.lower': 'format name to lower',
                   'for': 'loop the list to collect data'}

for glossary in python_glossary.keys():
    print(glossary.title())
'''

# 6-5
'''
river = {'nile': 'egypt',
         'amazon': 'south america',
         'chang jiang': 'china'}
for name, country in river.items():
    print("The " + name.title() + " runs through " +
          country.title() + "!")

print("\nName of rivers:")
for name in river.keys():
    print(name.title())

print("\nName of the country:")
for country in river.values():
    print(country.title())
'''

# 6-6
'''
people = {
    "me": {
        'first_name': 'simon',
        'last_name': 'law',
        'age': 19,
        'city': 'hong kong'
        },

    "mary": {
        'first_name': 'mary',
        'last_name': 'ho',
        'age': 23,
        'city': 'tokyo'
        },

    "tom": {
        'first_name': 'tom',
        'last_name': 'chan',
        'age': 20,
        'city': 'new york'
        }
    }

for people_name, people_info in people.items():
    print('Name: ' + people_name.title())
    full_name = people_info['first_name'] + " " + people_info['last_name']
    age = people_info['age']
    city = people_info['city']

    print('\tFull name: ' +  full_name.title())
    print('\tAge: ' + str(age))
    print("\tCity: " + city.title())
'''

# 6-8
'''
pets = {
    'fat_b': {
        'type': 'cats',
        'owner': 'simon'
    },

    'bobo': {
        'type': 'dogs',
        'owner': 'simon'
    },

    'oppa': {
        'type': 'dogs',
        'owner': 'swc'
    },
}

for pet_name, pet_info in pets.items():
    print("Pet's name: " + pet_name.title())
    types = pet_info['type']
    owner = pet_info['owner']

    print("\t" + pet_name.title() + " is a " + types + "!")
    print("\t" + pet_name.title() + " belongs to " + owner.title() + "!")
'''

# 6-9
'''
favorite_places = {
    'simon': ['osaka', 'thailand', 'paris'],
    'tom': ['new york', 'poland', 'italy'],
    'mary': ['london', 'india', 'singapore']
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place.title())
'''

# 6-10
'''
favorite_number = {'tom': [1, 7, 9],
                   'amy': [2, 4, 6],
                   'simon': [3, 24, 49],
                   'mary': [4, 16, 54],
                   'jack': [5, 25, 125]
                   }

for name, numbers in favorite_number.items():
    print("\n" + name.title() + "'s favorite numbers are: ")
    for number in numbers:
        print("\t" + str(number))
'''

# 6-11
'''
cities = {
    'tokyo': {
        'country': 'japan',
        'population': 9262046,
        'fact': "It's the capital of Japan."
    },

    'hong kong': {
        'country': 'china',
        'population': 7347000,
        'fact': "The property price is too high here!"
    },

    'new york': {
        'country': 'america',
        'population': 8538000,
        'fact': "Weed in here is legal!"
    },
}

for city_name, city_info in cities.items():
    print("\nHere is the info of " + city_name.title() + ": ")
    country = city_info['country']
    population = str(city_info['population'])
    fact = city_info['fact']
    print("\tCountry: " + country.title())
    print("\tPopulation: " + population)
    print("\tFact: " + fact)
'''

# 6-12
'''
skipped
'''

# 7-1
'''
car = input("What car do you want to rent? ")

print("\nLet me see if I can find you a " + car.title())
'''

# 7-2
'''
people = input("How many people do you have? ")
people = int(people)

if people >= 8:
    print("Sorry, We don't have emtpy tables now.")
else:
    print("Tables are available!")
'''

# 7-3
'''
number = input("Input a number and i tell you if it's a factor of 10: ")
number = int(number)

if number % 10 == 0:
    print("\t" + str(number) + " is the factor of 10!")
else:
    print("\t" + str(number) + " is not a factor of 10...")
'''

# 7-4
'''
toppings = "\nWhat would you want to add to your pizza?"
toppings += "\nEnter 'quit' to exit the program. "
message = ""
while message != 'quit':
    message = input(toppings)

    if message != 'quit':
        print("We will add " + message + " into your pizza!")
'''

# 7-5
'''
age = input("How old are you? ")
age = int(age)

if age <= 3:
    print("Your price will be free!")
elif age <= 12:
    print("Your price will be 10.")
else:
    print("Your price will be 15.")
'''

# 7-6
# Version 1
'''
toppings = "\nWhat would you want to add to your pizza?"
toppings += "\nEnter 'quit' to exit the program. "
message = ""

while message != 'quit':
    message = input(toppings)

    if message != 'quit':
        print("We will add " + message + " on your pizza!")
'''

# Version 2
'''
toppings = "\nWhat would you want to add to your pizza?"
toppings += "\nEnter 'quit' to exit the program. "

active = True
while active:
    message = input(toppings)
    if message == 'quit':
        active = False
    else:
        print("We'll add " + message + " on your pizza!")
'''

# Version 3
'''
toppings = "\nWhat would you want to add to your pizza?"
toppings += "\nEnter 'quit' to exit the program. "

while True:
    message = input(toppings)

    if message == 'quit':
        break
    else:
        print("We'll add " + message + " on your pizza!")
'''

# 7-7
'''
x = 1
while x <= 5:
    print(x)
    x += 1
'''

# 7-8
'''
sandwich_orders = ['subway', "mcdonald's", 'fuck']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print("We are making " + current_order + " for you now...")
    finished_sandwiches.append(current_order)

for finished_sandwich in finished_sandwiches:
    print("\tI made you a " + finished_sandwich + " sandwich!")
'''

# 7-9
'''
sandwich_orders = ['subway', 'pastrami', "mcdonald's", 'pastrami', 'fuck', 'pastrami']
finished_sandwiches = []
print('\nThe pastrami sandwich was sold out!\n')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print("We are making " + current_order + " for you now...")
    finished_sandwiches.append(current_order)

for finished_sandwich in finished_sandwiches:
    print("\tI made you a " + finished_sandwich + " sandwich!")
'''

# 7-10
'''
responses = {}

report_active = True

while report_active:
    name = input("\nWhat's your name: ")
    response = input("If you could visit one place in the world, where would you go? ")

    responses[name] = response

    repeat = input("Would you like to invite your friends to play? yes/ no:")
    if repeat == "no":
        report_active = False

print("--- Result ---")
for name, response in responses.items():
    print(name.title() + " would like to go " + response.title() +
          " for vacation!")
'''

# 8-1
'''
def display_message(name):
    print("Fuck you! " + name.title())

display_message('LMY')
'''

# 8-2
'''
def favorite_book(title):
    print("One of my favorite book is " + title.title() + "!")

favorite_book('alice in wonderland')
'''



















