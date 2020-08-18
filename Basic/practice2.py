## If
# if the condition is satisfied with the first statement, 
# it doesn't go further anymore even if secend statement is true.  

weather = "Sunny"
if weather == "rainny":
    print("Take an umbrella ")
elif weather == "finedust":
    print("Wear a mask")
else:
    print("You don't need anything.")

# temp = int(input("What is the temperature now?"))
temp = 15
if temp >= 30:
    print("It's too hot. Don't go out.")
elif 10 <= temp and temp < 30:
    print("Nice weather!")
elif 0 <= temp < 10:
    print("Bring your Coat.")
else: 
    print("It's too cold!. Don't go out.")


## For

for waiting_no in range(1,6):
    print("waiting number : {}".format(waiting_no))


starbucks = ["Iron Man", "Thor", "Groot"]
for customer in starbucks:
    print("{}, your coffee is ready to go".format(customer))

## While

customer = "Thor"
index = 5
while index >= 1:
    print("{0}, your coffee is ready. {1} left.".format(customer,index))
    index -=1
    if index == 0:
        print("Your coffee is gone.")


# customer = "Iron Man"
# index = 1
# while True:
#    print("{0}, your coffee is ready. calling {1}.".format(customer, index))
#    index -=1


customer = "Thor"
person = "unknown"

while person != customer:
    print("{0}, your coffee is ready.".format(customer))
   # person = input("What is your name?")
    person = "Thor"


absent = [2, 5]
no_book = [7] # forgot to bring a book
for student in range(1, 11): #1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue
    elif student in no_book:
        print("Let's call it a day! Follow me, {0}.".format(student))
        break
    print("{0}, read a bood.".format(student))

## For (one line)

students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students) # [101, 102, 103, 104, 105]

students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students) # [8, 4, 10]

students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students) # ['IRON MAN', 'THOR', 'I AM GROOT']

## Quiz 5
from random import *

passengers = []
total_pass = 0
for i in range(50):
    passengers.append(randint(5,50))
    if 5 <= passengers[i] <= 15:
        print(f"[O] passenger{i+1} (service time : {passengers[i]})")
        total_pass += 1
    else:
        print(f"[ ] passenger{i+1} (service time : {passengers[i]})")

print(f"Total passengers' number is {total_pass}.")
    