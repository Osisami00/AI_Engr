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
    "math" : int(input("Enter your math score: ")),
    "English" : int(input("Enter your English score: ")),
    "French" : int(input("Enter your French score: "))
}

total_score = student["subject"]["French"] + student["subject"]["math"] + student["subject"]["English"]
score_len = len(student["subject"])
student["passed"] = student["subject"]["math"] >= 50 and student["subject"]["English"] >= 50 and student["subject"]["French"] >= 50 
print(f"\nName : {student["name"]}\nAge: {student["age"]}\nSubject:\nMath: {student["subject"]["math"]}\nEnglish: {student["subject"]["English"]}\nFrench: {student["subject"]["French"]}\nAverage Score: {total_score/score_len: .1f}")

while True:
    if student["passed"] == True:
        print("Status: Promoted To The Next Class.")
        break
    else: 
        print("Your score is below average.\nStatus: To Repeat Class.")
        break


# Stationery Store Inventory Database
store ={"Book": 10, "Pen": 20, "Bag": 5, "Eraser": 10, "sellotape": 12}
# prompt user to enter item and quantity

while True:
    item_request = input("Enter the name of stationary you want to buy: ")
    if item_request.title() not in store:
        print(f"Feedback: We do not have {item_request.title()}s at the moment.")
    else:
        item_quantity = int(input(f"How many {item_request}s do you want to buy: "))
        break
    
while store[item_request] >= item_quantity:
    print(f"{item_request} bought successfully!")

else:
    print(f"We have {store[item_request]} available.")

# item_quatity = input("Enter qauntity of the item you want to buy: ")
