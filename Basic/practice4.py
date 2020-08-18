## File input and output

'''
Ceate score.txt file. 
score.txt
Math : 0
English : 50 
'''
score_file = open("score.txt", "w", encoding="utf8")
print("Math : 0", file=score_file)
print("English : 50", file=score_file)
score_file.close()


'''
Append the contents into score.txt file.
score.txt
Math : 0
English : 50
Science : 80
Coding : 100
'''
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("Science : 80")
score_file.write("\nCoding : 100")
score_file.close()

'''
Read all in the file.
Math : 0
English : 50
Science : 80
Coding : 100
'''
score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.read())
score_file.close()

'''
Read one line in the file.
Math : 0
English : 50
Science : 80
Coding : 100
'''
score_file = open("score.txt", "r", encoding = "utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

'''
Read one line in the file.
Math : 0
English : 50
Science : 80
Coding : 100
'''
score_file = open("score.txt", "r", encoding = "utf8")
lines = score_file.readlines() # save in list type
for line in lines:
    print(line, end="")
score_file.close()


## Pickle
import pickle
profile_file = open("profile.pickle", "wb")
profile = {"name":"Blair", "age":30, "hobbies":["soccer", "coding", "singing"]}
print(profile)
pickle.dump(profile, profile_file) # save profile info into the file.
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # Read the file into profile
print(profile) # {'name': 'Blair', 'age': 30, 'hobbies': ['soccer', 'coding', 'singing']}
profile_file.close() 

## With
# don't need to close 
import pickle
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file)) # {'name': 'Blair', 'age': 30, 'hobbies': ['soccer', 'coding', 'singing']}


# Create study.txt file with the contents
'''
study.txt
I'm studying Python so hard
'''
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("I'm studying Python so hard")

# Read study.txt
with open("study.txt", "r", encoding='utf8') as study_file:
    print(study_file.read()) # I'm studying Python so hard


## Quiz 
# You have to make a report once a week.
# Report format should be like this below.
# - Week 1 : Weekly Report -
# Department :
# Name :
# Work Summary : 
# 
# Create a program that generages week 1 to 50 weekly report.
# File name should be "Week1-Report.txt", "Week2-Report.txt" ...

for i in range(1,51):
    with open("Week"+str(i)+".txt", "w", encoding='utf') as report_file:
        report_file.write("- Week {} : Weekly Report -".format(i))
        report_file.write("\nDepartment :")
        report_file.write("\nName :")
        report_file.write("\nWork Summary :")

