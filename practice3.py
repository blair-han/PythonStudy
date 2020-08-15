@@ -0,0 +1,102 @@
##
'''
deposit successfully. Your balance is $20.
withdraw successfully. Your balance is $10
commission is $1, and balance is $4.
'''
def open_account():
    print("new account is created")

def deposit(balance, money):
    print("deposit successfully. Your balance is ${0}.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if(balance >= money):
        print("withdraw successfully. Your balance is ${0}".format(balance - money))
        return balance - money
    else:
        print( "withdraw fail! Your balance is ${0}".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 1
    return commission, balance - money - commission

balance = 0 
balance = deposit(balance, 20)
balance = withdraw(balance, 10)
commission, balance = withdraw_night(balance, 5)
print("commission is ${}, and balance is ${}.".format(commission, balance))


'''
name : Blair    age : 21        main language: Python
name : Paul     age : 21        main language: Python
name : Shin     age : 25        main language: Java
'''
def profile(name, age = 21, main_lang = "Python"):
    print("name : {}\tage : {}\tmain language: {}" \
        .format(name,age,main_lang))

profile("Blair")
profile("Paul")
profile(age = 25, name = "Shin", main_lang="Java")


'''
name : Blair    age : 20        PythonJavaCC++Javascript
name : Clair    age : 29        KotlinSwiftC#
'''
def profile(name, age, *argv):
    print("name : {}\tage : {}\t".format(name,age), end="")
    for lang in argv:
        print(lang, end = "")
    print()

profile("Blair", 20, "Python", "Java", "C", "C++", "Javascript")
profile("Clair", 29, "Kotlin", "Swift", "C#")


## Global variable & Local variable
gun = 10
def checkpoint(soldiers):
    global gun 
    gun = gun - soldiers
    print("(in the function) The total number of guns : {}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("(in the function) The total number of guns : {}".format(gun))
    return gun

print("The total number of gun : {}".format(gun))
checkpoint(2)
gun = checkpoint_ret(gun, 3)
print("gun left : {}".format(gun))


## Quiz 6
# create a program that calculates Standard weight.
#
# Formula
# Male : height(m) * height(m) * 22
# Female : height(m) * height(m) * 21
# 
# Condition 1: make function to calculate standard weight.
#              Parameter : height, gender 
# Condition 2 : Calculate it to two decimal places.

def std_weight(height, gender):
    if gender == "male":
        return height * height * 22
    else:
        return height * height * 21

height = 175 # cm
gender = "male"
weight = round(std_weight(height / 100, gender), 2)
print("The standard weight of height {0}cm {1} is {2}kg.".format(height, gender, weight))


    