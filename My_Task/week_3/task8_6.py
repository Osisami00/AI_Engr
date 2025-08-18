# Task6: Eligibility Checker
# create empty dict
student = {}
# ask user to enter their details
student["name"]  = input("Enter your name: ")
student["age"] = int(input("Enter your age: "))
student["waec_result"] = bool(input("Did you pass all your required subjects: "))
student["jamb_score"] = int(input("Enter your Jamb score: "))
student["post_utme"] = int(input("Enter your Post-UTME score: "))

# place entries alongside requirment
age_eligibility = student["age"] >= 16
waec_eligibility = student["waec_result"] == True
jamb_eleigibility = student["jamb_score"] >= 200
post_utme_eligibility = student["post_utme"] >= 200
# set total eligibility
total_eligibility = age_eligibility and waec_eligibility and jamb_eleigibility and post_utme_eligibility
# printstudent details with admission eligibility status
print(f"Name: {student['name']}\nAge: {student['age']}\nWAEC Result:{student["waec_result"]}\nJamb Score:{student["jamb_score"]}\nPost-UTME Score:{student["post_utme"]}\nAdmission Status: {total_eligibility}")

