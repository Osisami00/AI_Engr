# Task 4
# creat an empty dict call student
student = {}
# promt users to enter details
name = input("Enter name: ")
age = int(input("Enter age: "))

# input response into dict
student["name"] = name
student["age"] = age
# set score list
score = [15, 85, 90]
# input score into dict
student["score"] = score
# create pass calculator
passed = score[0] >= 50 and score[1] >= 50 and score[2] >= 50
# create teenager identifier
teenager = student["age"] >= 13 and student["age"] <=19
# print in f-string
print(f"Student Recod:\nName:\t{name}\nAge:\t{age}\nScores:\t{score}\nPassed:\t{passed}\nTeenager:\t{teenager}")
