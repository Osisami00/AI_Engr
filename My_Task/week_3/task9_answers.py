# Simulated USSD Menu Interaction
'''
print("Yello! Dial *556# for data and other services")

ussd_code = "*556#"
ussd_request = input("Yello! enter ussd code: ")

while ussd_request != ussd_code:
    print("You entered the wrong code.")
    ussd_request = input("Yello! enter ussd code: ")

    



balance = 500   
airtime = []
data_amount = []



print("Yello Customer! What would you like to do today: ")
print("1. Check Balance")
print("2. Buy Airtime")
print("3. Buy Data")

ussd_request = input("Enter a number: ")
user_name = input("Kindly sign-up before using our service.\nEnter your name: ")
phone_num = int(input("Enter your phone number: "))
password_request = input("Enter password: ")

print(f"\n\nYello Customer! What would you like to do today: ")
print("1. Check Balance")
print("2. Buy Airtime")
print("3. Buy Data")


if ussd_request == "1": 
    print(f"Your balance is {balance}.")
elif ussd_request == "2":
    airtime =input("How much airtime do you want to buy: ")
    print(f"Your airtime purchase of #{airtime} is succesful")
elif ussd_request =="3":
    data_amount = int(input("How much data do you want: "))
    if data_amount >= balance :
        print(f"Insufficient Balace. Your available balance is #{balance}. Buy #{data_amount-balance} airtime to buy #{data_amount} data.")
    else:
        print(f"Data bought successfully!")
else: 
    print("Enter a valid number.")




# Task6-Question 3 - Football Match System
# **Task3: Simulate a football match ticket system**

# - Store all seat numbers (1 to 50) in a set.

# - Ask users to "book" a seat by entering the number.

# - Remove booked seats from the set.

# - Show remaining seats after each booking.



print("Dial *222# to book a football ticket")
dial_code = "*222#"
dial_code_request =input("Enter ticket dial code: ")

while dial_code_request != dial_code:
    dial_code_request = input("Enter ticket dial code: ")
    

# ticket_number = set(range(1,50))
ticket_number = set([i for i in range(1,51)])
booking_request = int(input("Book a seat number from 1-50: "))

while True: 
    if booking_request in ticket_number:
        print(f"Your ticket is booked succesful!")
        break
    else: 
        booking_request = int(input("Book a seat numbe 1-50: ")) 
    
unbooked_number_request = int(input("Enter 1 to check available seat numbers: "))
ticket_number.remove(unbooked_number_request)
while unbooked_number_request == 1:
    print("The available seat numbers are: ", ticket_number, sep=",")
    print("Good Bye!")
    break
else: 
    unbooked_number_request = int(input("Enter 1 to check available number: "))



# Task6 -Question 4: Unique Voters Registration
# - Ask for voter names and store in a set.

# - If a voter tries to register twice, display a warning.

# - After registration, display the total number of unique voters.

# print("Welcome to INEC registration exercise")
# voters_bio = set()
# # name = set()
# for i in range(1,6):
#     name = set(input("Enter your name: "))

# # while i
#     # age = input("Enter your age: ")




# Task8 Exercise 2: FG Scholarship Elegibility
# prompt student for bio
student_bio = {}

print("Welcome to our Scholarship Selection Process.")
print("Fill in the next details to the best of your knowledge.")
student_bio["name"] = input("Enter your name: ")
student_bio["age"] = int(input("Enter your age: "))
student_bio["nationality"] = bool(input("Are you a Nigerian: "))
student_bio["waec_status"] = bool(input("Do you pass all your WAEC compulsory subjects: "))
student_bio["scholarship_status"] = bool(input("Are you currently on a local or international scholarship: "))

print("\nChecking Eligibity Status...")

if student_bio["age"] <= 15:
    print("Age: lower than required\nPoint Awarded: 0")
elif student_bio["age"] >= 25:
    print ("Age: Greater than Required\nPoint Awarded: 0")
else:
    print("Age: Accepted\nPoint Awarded: 20 Awarded")

while student_bio["nationality"] == "Yes":
    print("Nationality: Nigerian\nAwarded Point: 20")
    break
else: 
    print("Nationality: Not Nigerian\nPoint Awarded: 0")
while student_bio["waec_status"] == "Yes":
    print("WAEC Status: True\nPoint: 20points awarded")
if student_bio["scholarship_status"] == "Yes":
    print("Scholarshoip Status: Active\nPoint Awarded: 0")
else:
    print("Scholarship Status: Inactive\nPoint Awarded: 20")
eligibility_status = student_bio["age"] and student_bio["nationality"] and student_bio["waec_status"] and student_bio["scholarship_status"]

print(f"Eligibity Status: {eligibility_status}")
'''


# **Task8 Exercise4: Student Record**
# - Create an empty dictionary called student.

# - Ask the user to input their name and age, then store them in the dictionary.

# - Add a list of scores (e.g., [70, 85, 90]) to the dictionary.

# - Use a comparison operator to check if the student has passed (average score >= 50). Save the result (True/False) in the dictionary under the key "passed".

# - Use a logical operator to check if the student is a teenager (age between 13 and 19). Save the result as "teenager".

# - Print out the complete record in this format:


student = {}

student["name"]= input("Enter your name: ")
student["age"] = input("Enter your age: ")
student["subject"] = {
    "math" : int(input("Enetr your math score: ")),
    "English" : int(input("Enetr your English score: ")),
    "French" : int(input("Enetr your French score: "))
}
student["passed"] = student["subject"]["math"] >= 50 and student["subject"]["English"] >= 50 and student["subject"]["French"] >= 50 
print(f"\nName : {student["name"]}\nAge: {student["age"]}\nSubject:\nMath: {student["subject"]["math"]}\nEnglish: {student["subject"]["English"]}\nFrench: {student["subject"]["French"]}")

while True:
    if student["passed"] == True:
        print("You are promoted to the next class")
        break
    else: 
        print("You need be more serious to get promoted next year")
        break


