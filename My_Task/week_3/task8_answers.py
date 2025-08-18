# Task 1 
# Explain each output of the program below:
# Give 3 use cases or scenarios where you can apply the program
# Write the program for 1 

'''
# The code below is used to prompt users to enter the first and second number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# The code below is used to compare the first and second number 
print(f"{num1} == {num2} : {num1 == num2}")

# The code below states that num1 is not equals to num2
print(f"{num1} != {num2} : {num1 != num2}")

# The code below shows that num1 is less than num2
print(f"{num1} < {num2} : {num1 < num2}")

# USe CAses
# 1- Market Budget
# 2- Basic Calculator
3- 


# Market Budget
# request price for first item
rice = float(input("Enter amount of money you budget for Rice: "))
beans = float(input("Enter the amount of money you budget for beans: "))

print(f"{rice} > {beans} : {rice > beans}")



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




# Task3: Online Store Cart Calculator
item_list = ["Book", "Pen", "Bag"]
item_price = [500,100,800]
cart_total = 0
cart_total += item_price[0] + item_price[1] + item_price[2]
print(f"Items : {item_list}\nTotal Price: {cart_total}")


# Task 4
# creat an emoty dict call student
student = {}
name = input("Enter name: ")
age = int(input("Enter age: "))
student["name"] = name
student["age"] = age

score = [15, 85, 90]

student["score"] = score

passed = score[0] >= 50 and score[1] >= 50 and score[2] >= 50

teenager = student["age"] >= 13 and student["age"] <=19
print(f"Student Recod:\nName:\t{name}\nAge:\t{age}\nScores:\t{score}\nPassed:\t{passed}\nTeenager:\t{teenager}")



# Task5: Store Inventory Update

store_item = {"Book": 10, "Pen": 15, "Bag": 12}
item_request = input("Enter item name: ")
quantity_request = int(input("Enter the quantity you want: "))
print(f"Before purchase: {store_item}")
store_item[item_request.title()] -= quantity_request
 
print(f"After purchase: {store_item}")
'''

# Task6: Eligibility Checker
student = {}
student["name"]  = input("Enter your name: ")
student["age"] = int(input("Enter your age: "))
student["waec_result"] = bool(input("Did you pass all your required subjects: "))
student["jamb_score"] = int(input("Enter your Jamb score: "))
student["post_utme"] = int(input("Enter your Post-UTME score: "))

age_eligibility = student["age"] >= 16
waec_eligibility = student["waec_result"] == True
jamb_eleigibility = student["jamb_score"] >= 200
post_utme_eligibility = student["post_utme"] >= 200
total_eligibility = age_eligibility and waec_eligibility and jamb_eleigibility and post_utme_eligibility
print(f"Name: {student['name']}\nAge: {student['age']}\nWAEC Result:{student["waec_result"]}\nJamb Score:{student["jamb_score"]}\nPost-UTME Score:{student["post_utme"]}\nAdmission Status: {total_eligibility}")








