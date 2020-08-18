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

##
print("Python", "Java", sep=", ", end ="? ")
print("Which one is more fun")  # Python, Java? Which one is more fun


import sys
print("Python", "Java", file=sys.stdout) # Python Java 
print("Python", "Java", file=sys.stderr) # Python Java

# test score
'''
Math 0
English 50
Coding 100

Math     :    0
English  :   50
Coding   :  100
'''
scores = {"Math":0, "English":50, "Coding":100}
for subject, score in scores.items():
    # print(subject, score) # English 50 
    print(subject.ljust(8), str(score).rjust(4), sep= " : ") 


## Waiting numbers
# 001, 002,  003, ...
'''
Wating number : 001
Wating number : 002
Wating number : 003
Wating number : 004
Wating number : 005
Wating number : 006
Wating number : 007
Wating number : 008
Wating number : 009
Wating number : 010
Wating number : 011
Wating number : 012
Wating number : 013
Wating number : 014
Wating number : 015
Wating number : 016
Wating number : 017
Wating number : 018
Wating number : 019
Wating number : 020
'''
for num in range(1, 21):
    print("Wating number : " + str(num).zfill(3))


## Input function
# return string type
# answer = input("type any value : ")
# print("Whay you typed is : " + answer + ".")



# leave empty space empty space, right alignment, total 10 
print("{0: >10}".format(500))
# 오른쪽 정렬, 10자리 확보, 부호 붙이기 빈자리는 빈칸으로 채우기 
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# right alignment 10자리 확부, 부호붙이기, 빈자리는 _로 채우기
print("{0:_<+10}".format(500))
# 3자리마다 콤마찎기
print("{0:,}".format(100000000)) # 100,000,000
# 3자리마다 콤마 찍기, +-부호 붙이기
print("{0:+,}".format(100000000)) # +100,000,000
print("{0:+,}".format(-100000000)) # -100,000,000
# 3자리마다 콤마 찍기, 부호 붙이기, 자릿수 확부
# 빈자리는 ^ 채우기
print("{0:^<+30,}".format(-100000000)) # -100,000,000^^^^^^^^^^^^^^^^^^
# 소수점 출력
print("{0:f}".format(5/3)) # 1.666667
# 소수점 특정 자리수 까지만 표시 (소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5/3)) # 1.67

