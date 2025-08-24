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
