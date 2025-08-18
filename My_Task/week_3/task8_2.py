# Task 2i

#This used to promt users to enter their details
name = input("Enter your name: ")
age = int(input("Enter your age: "))
score = int(input("Enter your test score: "))

# This is used to compare the age entered by the user to 
# the required age of 18 and the score to the required number of 70
eligibility = (age < 18) and (score > 70)
# f string  is use to print the details of the user with the eligibility status
print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")



# Task2ii: Citizenship

#This used to promt users to enter their details

# prompt users for details
name = input("Enter your name: ")
age = int(input("Enter your age: "))
citizenship = bool(input("Enter True if you are Nigerian citizen or False if otherwise: "))
uni_registered= bool(input("Enter True if you are resisted in Nigerian University:"))
scholarship_status = bool(input("Enter True if you are currently on a scholarship or False if otherwise: "))
waec_qualification = bool(input("Enter True if you pass you five core WAEC subjects or False if otherwise:"))
# create programme for qaulification status
qualification_status = (f"{name} qualification status: {citizenship and uni_registered and scholarship_status and waec_qualification }")
print(qualification_status)