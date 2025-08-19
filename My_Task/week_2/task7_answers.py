# Task1: Student Bio Data Storage
'''
# create empty dict
student_bio = {}
# collect student bio and update i
student_bio.update({"name" : input("Hi! Kindly enter your name: ")}),
student_bio.update({"age" : int(input("Enter your age: "))}),
student_bio.update({"sex": input(("What is your gender? "))}),
student_bio.update({"course_title" : input("Enter course of study:")})
# compile student bio and print on diff lines
compiled_bio = "\n".join(f"{key}:\t{value}" for key,value in student_bio.items())
print(compiled_bio)


# Task2: super Market PRice list
item_list=["bama", "butter", "oil"]

# request items
first_item_price = int(input("Enter the price of Bama: "))
second_item_price = int(input("Enter the price of Butter: "))
third_item_price = int(input("Enter the price of Oil: "))

dict_of_items = {}
dict_of_items[item_list[0]] =first_item_price
dict_of_items[item_list[1]] = second_item_price
dict_of_items[item_list[2]] = third_item_price

print(dict_of_items)
name_update = input("Enter the name of item you want to change: ")
price_update = input("Enter the updated price of the item you entered: ")

# print(name_update in dict_of_items.keys())

dict_of_items.update({name_update : price_update})
print(dict_of_items)


# Task3: Day And Activities Pairing
days =("Sunday", "Monday", "Tuesday", "Wednesday","Thursday","Friday")
# collect active days  from users
day1 = input('Enter first day of the week where you perform an activity: ')
day2 = input('Enter second day of the week where you perform an activity: ')
day3 = input('Enter third day of the week where you perform an activity: ')

# collect activity data from users
activity1 =input("Enter activity for day one: ")
activity2 =input("Enter activity for day two: ")
activity3 = input("Enter acyivity for day three :")

# save data in tuple
active_days =(day1,day2,day3)
activities =(activity1, activity2,activity3)
print({day: activity for day, activity in zip(active_days, activities)})

# Task4 : Unique Members Registration

# request for name
names = input("Enter three names separated with comma: ")
# split names in the tuple
names_set = set(names.split(","))
names_set = set(name.strip() for name in names_set)
# make the length of each name be the value for each name
name_dict = {name: len(name) for name in names_set}
print(name_dict)




# Compulsory Task: Student Profile Builder
# collect student info
student_info = ()
student_name = input("Enter your name: ")
student_age = int(input("How old are you: "))
student_sex = input("Enter sex: ")

# collect subject info
subject_info = ()
subject1_name = input("Enter first subject: ")
subject2_name = input("Enter second subject: ")
subject_name =subject1_name, subject2_name
subject_score = ()
subject1_score = input("Enter score for subject one: ")
subject2_score = input("Enter score for subject two: ")
subject_score =subject1_score, subject2_score

subject_info = subject_name, subject_score
subject_info = ",".join()

'''
# collect Guardian Info
guardian_info = ()
guardian_name = input("Enter guardian name: ")
guardian_no = input("Enter guardian phone number: ")

# collect Student's Hobbies Info
hobbies = input("Enter three hobbies: ")
'''


#Collect Basic Info
name = input('Enter student\'s name here: ')
age = int(input('Enter student\'s age here: '))
gender = input('Enter student\'s gender here: ')
class_ = input('Enter student\'s class here: ')

#Collect scores for subjects
subjects = ('maths', 'eng', 'bio', 'chem', 'phy')

scores = tuple(float(input(f'Enter score for {subject}: ')) for subject in subjects)

#Guardian info
Guardian_name = input('Enter guardian name here: ')
Guardian_phone_num = input('Enter guardian phone number here: ')

#hobbies
hobbies = set(input('Enter hobbies seperated by commas: ').split(','))
hobbies = tuple(hobby.strip() for hobby in hobbies)

class_profile = {'Basic Info': {'Name': name.title(), 'Age': age, 'class': class_, 'Gender': gender}, 'Performance': {subject: score for subject, score in zip(subjects, scores)}, 'Guardian info': {'Guardian name': Guardian_name.title(), 'Guardian Phone number': Guardian_phone_num}, 'Hobbies': list(hobbies)}

#Derived Data
class_profile["Performance"]["Average"] = sum(scores) / len(scores)
class_profile["Basic Info"]["Initials"] = "".join([n[0] for n in name.split()])
class_profile["Hobbies Count"] = len(hobbies)

#Output
title = 'Student Profile'
title2 = 'Student\'s Performance'
title3 = 'Guardian Information'
title4 = 'Hobbies'


print('\n')
print(f'{title:^50}')
print(f"Name: {class_profile['Basic Info']['Name']:>44}")
print(f"Age: {class_profile['Basic Info']['Age']:>45}")
print(f"Gender: {class_profile['Basic Info']['Gender']:>42}")

print('\n')
print(f'{title2:^50}')
print(class_profile["Performance"])

print('\n')
print(f'{title3:^50}')
print(class_profile["Guardian info"])

print('\n')
print(f'{title4:^50}')
print(class_profile["Hobbies"])
print(f"\nTotal Hobbies:\t{class_profile['Hobbies Count']}")
print(f"Average Score:\t{class_profile['Performance']['Average']:.2f}")
'''