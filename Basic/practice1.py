'''
Basic Practice
'''

# Number
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

# String
print('baloon')
print("butter")
print("ha"*9)

# Boolean
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not False)

# Variable
animal = 'dog'
name = 'Choco'
age = 8
hobby = "walking"
is_puppy = age <=1

print(f"My {animal}'s name is {name}.")
#print(f"{name} is {age} years old and she likes {hobby}.")
#print(name + " is " + str(age) + " year-old and" + name +" likes " + hobby +".")
print(name, " is ", age,  " year-old and", name, " likes ", hobby, ".")
print(f"Is {name} a puppy? {is_puppy}")


# Quiz1
station = ["Redfun", "Central", "Townhall"]
for i in range(len(station)):
    print("The train heading to ", station[i], "is coming.")

# Operator
print(1 + 1) #2 (plus)
print(3 - 2) #1 (minus)
print(5 * 2) #10 (multiply)
print(6 / 3) #2.0 (division)
print(2 ** 3) #8 (power)
print(5 % 3) #2 (remainder)
print(10 % 3) #1
print(5 // 3) #1 (quotient)
print(10 // 3) #3
print(10 > 3) #True
print(4 >= 7) #False
print(10 < 3) #False
print(5 <= 5) #True
print(3 == 3) #True (equal)
print(1 != 3) #True (not equal)
print(not(1 != 3)) #False
print((3 > 0) and (3 < 5)) #True 
print((3 > 0) & (3 < 5)) #True
print((3 > 0) or (3 > 5)) #True
print((3 > 0) | (3 > 5)) #True
print(5 > 4 > 3) #True
print(5 > 4 > 7) #False

number = 2 + 3 * 4 #14
print(number)
number = number + 2 #16
print(number)
number +=2 #18
print(number)
number *= 2 #36
print(number)
number /= 2 #18.0
print(number)
number -= 2 #16.0
print(number)
number %= 5 #1.0
print(number)

# Function for numbers
print(abs(-5)) #5
print(pow(4,2)) # 4 ^ 2 = 4 * 4 = 16
print(max(5, 12)) #12
print(min(5, 12)) #5
print(round(3.14)) #3
print(round(4.99)) #5

from math import *
print(floor(4.99)) #4
print(ceil(3.14)) #4
print(sqrt(16)) #4.0

# Random function
from random import *
print(random()) # 0.0 ~ 1.0 random number
print(random() * 10) #0.0 ~ 10.0 random number
print(int(random() * 10)) # 0 ~ 10 random integer number

print(int(random() * 45) +1) # 1~45 random integer number
print(randrange(1, 46)) #1~45 random integer number
print(randint(1, 45)) #1~45 random integer number

# Quiz2
# You are going to have a meeting with your study mates.
# Pick the date randomly. 
# Condition 1 : You have to use the random function.
# Cndition 2 : day should be 4 - 28 of this month.
# Condition 3 : print format is "We are gonna meet on 20th of this month."


from random import *
meeting = randint(4,28)
print(f"We are gonna meet on {meeting}th of this month.")


# String
sentence1 = "I'm a boy."
print(sentence1)
sentence2 = "Python is easy."
print(sentence2)
sentence3 = """
I'm a boy,
and Python is easy
"""
print(sentence3) # 4 lines

# Parcing
jumin = "880111-1111111"
print('Sex : ' +jumin[7]) #1
print("Year : " + jumin[0:2]) #88
print('Month : ' + jumin[2:4]) #01
print("Day : " + jumin[4:6]) #11
print("Date of Birth :" +jumin[:6]) #880111 first to 5
print("Last 7 numbers :" + jumin[7:]) # 1111111 7 to end
print("Last 7 numbers :" + jumin[-7:]) #1111111 -7 to end

# Function for String
python = "Python is Amazing"
print(python.lower())  #python is amazing
print(python.upper()) #PYTHON IS AMAZING
print(python[0].isupper()) #True
print(len(python)) #17
print(python.replace("Python", "Java")) #Java is Amazing

index = python.index('n') #location of "n" in python variable
print(index) #5
index = python.index("n", index+1) # location of "n" from 6th character in python variable
print(index) #15

print(python.find("Java")) # if there is no match then return -1
# print(python.index("Java")) #if there is no match then error

print(python.count("n")) # How many "n" does it have?


# How to print variable
# Method 1
print("a" + "b") # ab

# Method 2
print("a", "b") # a b
print("I am %d years old." % 20) # I am 20 years old.
print("I like %s." %"apple") # I like apple.
print("Apple starts with %c." % "A") # Apple starts with A.
print("I like %s and %s" %("blue","pink")) # I like blue and pink

# Method 3
print("I'm {} year-old.".format(20)) # I'm 20 year-old.
print("I like {} and {}.".format("blue","pink")) #I like blue and pink.
print("I like {0} and {1}.".format("blue","pink")) #I like blue and pink.
print("I like {1} and {0}.".format("blue","pink")) # I like pink and blue.
print("I'm {age} year-old and I like {colour}.".format(age=20, colour = "red")) # I'm 20 year-old and I like red.
print("I'm {age} year-old and I like {colour}.".format(colour = "red", age=20)) # I'm 20 year-old and I like red.

# Method 4
age = 20
colour = "red"
print(f"I'm {age} year-old and I like {colour}.") # I'm 20 year-old and I like red.

# \n : enter
print("Hello. \nHow are you?")

# \" \' 
print("I'm Blair") # I'm Blair
print('I\'m Blair') # I'm Blair

# \\ : back slash
print("C:\\Users\\Desktop\\PythonWorkspace") #C:\Users\Desktop\PythonWorkspace

# \r : carrage - return to the beginning of the current line.
print("Red Apple \rPine") # PineApple 

#\b : back space
print("Redd\bApple") # RedApple

#\t : Tab
print("Red\tApple") # Red     Apple


# Quiz3
# Make a program that generates a password based on URL.
# Ex) http://www.naver.com
# Condition 1 : Remove "http://" => naver.com
# Condition 2 : All characters after the first period should be removed. =>naver
# Condition 3 : first 3 characters of the rest + lenth of the rest + the number of e in the rest + "!" =>nav 5 1 !


url = "http://naver.com"

if int(url.find("http")) != -1:
    url = url.replace("http://","")
    print(url) 

if int(url.find(".")) != -1:
    url = url[:url.index(".")]
    print(url)

password = url[:3] + str(len(url)) + str(url.count("e")) + "!"
print(password) # nav51!

# List
subway = [10, 20, 30]
subway = [10]
print(subway)

subway = ["Blair", "Lilly", "Marry"]
print(subway) # ['Blair', 'Lilly', 'Marry']

# Where is Lilly?
print(subway.index("Lilly")) #1

# Add one more person at the end
subway.append("Patrick")
print(subway) # ['Blair', 'Lilly', 'Marry', 'Patrick']

# Add one person between Lilly and Marry
subway.insert(2, "Lynda")
print(subway) # ['Blair', 'Lilly', 'Lynda', 'Marry', 'Patrick']

# remove one person at the end
print(subway.pop()) # Patrick
print(subway) # ['Blair', 'Lilly', 'Lynda', 'Marry']

# Cound in the list
subway.append("Blair")
print(subway) # ['Blair', 'Lilly', 'Lynda', 'Marry', 'Blair']
print(subway.count("Blair")) #2

# Sort list
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# Sort reversly
num_list.reverse()
print(num_list) # [5, 4, 3, 2, 1]

# Delete all contents in the list
num_list.clear()
print(num_list) # []

# Merge two lists
num_list = [1, 5, 6]
mix_list = ["Blair", 20, True]
num_list.extend(mix_list)
print(num_list) # [1, 5, 6, 'Blair', 20, True]


# Dictionary
cabinet = {3:"Blair", 100:"John"}
print(cabinet[3]) # Blair
print(cabinet[100]) # John
print(cabinet.get(3)) # Blair
# print(cabinet[5]) # Error
print(cabinet.get(5)) # None
print(cabinet.get(5, "Available")) # Available
print(3 in cabinet) # True
print(5 in cabinet) # False

# Add dictionary
cabinet[5] = "Lilly"
print(cabinet) # {3: 'Blair', 100: 'John', 5: 'Lilly'}
cabinet[3] = "Chris"
print(cabinet) # {3: 'Chris', 100: 'John', 5: 'Lilly'}

# Remove dictionary
del cabinet[3]
print(cabinet) # {100: 'John', 5: 'Lilly'}

# Print key only
print(cabinet.keys()) # dict_keys([100, 5])

# Print value only
print(cabinet.values()) # dict_values(['John', 'Lilly'])

# Print key and value in pair
print(cabinet.items()) # dict_items([(100, 'John'), (5, 'Lilly')])

# Remove all contents in the dictionary
cabinet.clear()
print(cabinet) # {}

# Tuple 
menu = ("BBQ Pizza", "Potato Pizza")
print(menu[0]) # BBQ Pizza
print(menu[1]) # Potato Pizza
# menu.add("Peperoni Pizza") # Error

name = "Sally"
age = 20
hobby = "Coding"
print(name, age, hobby) # Sally 20 Coding

(name, age, hoby) = ("Blair", 30, "Cooking")
print(name, age, hobby) # Blair 30 Coding


## Set - no dup, no order
my_set = {1,2,3,3,3}
print(my_set) # {1, 2, 3}

java_developer = {"Blair", "Sally", "Ryon"}
python_developer = {"Blair", "Paul"}

# intersection
print(java_developer & python_developer) # {'Blair'}
print(java_developer.intersection(python_developer)) # {'Blair'}

# union
print(java_developer | python_developer) # {'Paul', 'Blair', 'Sally', 'Ryon'}
print(java_developer.union(python_developer)) # {'Sally', 'Blair', 'Ryon', 'Paul'}

# difference of set
print(java_developer - python_developer) # {'Sally', 'Ryon'}
print(java_developer.difference(python_developer)) # {'Ryon', 'Sally'}

# add set
python_developer.add("Sally") 
print(python_developer) # {'Paul', 'Sally', 'Blair'}

# remove set
python_developer.remove("Paul")
print(python_developer) # {'Blair', 'Sally'}


## Structure change
# Coffee shop
menu = {"Coffee", "Milk", "Juice"}
print(menu, type(menu)) # {'Coffee', 'Juice', 'Milk'} <class 'set'>

menu = list(menu)
print(menu, type(menu)) # ['Milk', 'Juice', 'Coffee'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu)) # ('Milk', 'Coffee', 'Juice') <class 'tuple'>

menu = set(menu)
print(menu, type(menu)) # {'Milk', 'Juice', 'Coffee'} <class 'set'>


## Quiz 4
# Your school is holding the Python coding contest
# To increase the participation rate, they decided to draw for four winnners.
# Chicken for one person, Coffee for three people. 
# Create a program
# Condition 1 : 20 people participated in this contest.
# Condition 2: randomly pick but no dup
# Condition 3 : use suffle and sample function from random module.

from random import *

# Step 1 - Generate participants list
participants = range(1, 21)
# print(type(participants)) # <class 'range'>
participants = list(participants)
# print(type(participants)) # <class 'list'>
# for i in range(1, 21):
#    participants.append(i)
print(participants) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Step 2
shuffle(participants)
print(participants) # [6, 15, 2, 5, 1, 19, 8, 7, 13, 14, 9, 4, 20, 12, 10, 3, 17, 16, 11, 18]

# Step 3
winners = sample(participants, 4)
print(winners) # [16, 2, 1, 5]

# Step 4
print("Winner for Chicken : {}".format(winners[0]))
print("Winners for Coffee : {}".format(winners[1:]))
print("--Congratulations--")
