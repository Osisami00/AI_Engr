# Task1: Student Bio Data Storage

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