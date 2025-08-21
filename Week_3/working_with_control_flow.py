# CONTROL FLOW IN PYTHON
# - Control flow refers to the order in which statements are executed in a program.
# Instead of always running line by line, control flow allows your program to:

#     - Make decisions (choose one path or another, explore alternatives).

#     - Repeat actions (loops).

#     - Exit or skip parts of code.
# CF is divided into 3
# A. CONDITIONAL STATEMENTS

'''
# 1. if statement  - Execute a block only when a condition is true
age = 20
if age >= 19:
    print("You are eligible to vote.")

# Use Cases:
# Check eligibility 
# Validating login attempt
# Ensuring a minimum purchaes requirement e.t.c


# 2- If - else statement : provides two alternative paths
wallet = 400
price = 500

if wallet >= price:
    print("Purchase succeful1")
else:
    print("Insuficient balance!")

# USe CASES
# Deciding succes or failure of payment
# Granting or denying aces to system

# 3- if-elif-else statement: use  for multiple conditions

score = 85
if score >= 70:
    print("Grade A")
elif score >= 50: 
    print("Grade B")
else:
    print("Grade C")

# Use CASES
# -student grading systems
# Assigning ticket categories(VIP,Regular,Student)
# categorizing temperature(Hot,Warm,Cold), et.c

# Nested If- Placing an if inside another if
age = 19
citizen = True

if age >=18:
    if citizen:
        print("You can vote.")
    else:
        print("You must be a citizen to vote")
else:
    print("Too young to vote")

# Use Cases
# Voting eligibility age+citizenship
# Banking(account active + balance sufficient)
# school admission (age + grade level)



# B. LOOP
# 1- for loop : This is used for iterating over a sequence (string, list,tuple,dictionary)

# iterate through each element in a LIST
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I love {fruit}")

# Use CAses:
# Iterating through shopping lists
# checking avalability of products

# iterate through each element in a TUPLE
# This works like list, but remember that tuples are immutatble

cordinates = (0.2233, -0.3444, 0.4544)

for point in cordinates:
    print(f"Point: {point}")
'''

# Iterates through each element in a DICT.
# Recall that dict have key-value pairs

# student = {"name": "Tunde", "age":12, "grade": "A"}
# for key in student.keys():
#     print(f"Keys: {key}")
# for value in student.values():
#     print(f"Values: {value}")
# for key,value in student.items():
#     print(f"{key}:{value}")

# Use Cases
# Reading database records.
# Showing user profile details
# checking configuration setting

# Iterate through each element in a STRING
# Remenber that strings are sequences of character

# word = "Python"
# for char in word:
#     print(char)

# USE CASES
# counting vowels/consonants
# Password validation(checking digits and special chars)
# Text analysis e.t.c



# 2- while loop
# A while loop is used to rpeatedly execute a block of codes as
# long as agivien condition is true. Unlike the FOR loop which iterates over 
# seaquence like list, tuplee.etc

# while condition:
    # code block
    # The condition must evaluate to True for the loop to continue running
    # When the condition becomes False the loop stops

# count = 1
# while count <= 5:
#     print("Number:", count)
#     count += 1

# Increment with "while"]
# num = 1
# while num <= 10:
#     print(num, end= "")
#     num +=1

# Decrementing with while
# timer = 10
# while timer > 0:
#     print("Countdown:", timer)
#     timer -=1

# while with user input 
# keep asking until the user enters a correct password

# password =""
# while password != "python123":
#     password = input("Enter the passwword: ")
# print("Access Granted")




# while True:
    # Code block 
    # Mustinclude a break statement to stop

# Keep asking the user for a name until the type "exit"
# while True:
#     name = input("Enter your name (type 'exit' to quit):")
#     if name.lower() == "exit":
#         print("Goodbye!")
#         break
#     print(f"Hello, {name}")


# Loop Control Statement (break, continue and pass)
# These keywords help us to control the behaviours of loops

# 1- BreAK: stop loop immediately. It is used if a condition is met
#  and there is no need to continu looping

# for num in range (1,10):
#     if num == 5:
#         print(num)

#The loop stops completely when num == 5.

# Stop searching when an item is found.

# Exit when user input matches a condition.

# Prevent unnecessary iterations.


# 2- CONTINUE : SKIPS THE CURRENT ITERATION AND MOVES TO THE NEXT ONE
# It is used if you want to ignore som values but keep the loop running
# for num in range(1,6):
#     if num == 3:
#         continue
#     print(num) 


# 3- PASS: Does nothing. A placeholder to avoid errors. 
# It is used if you haven't written the code yet want ot to keep the structure

# for num in range(1,6):
#     if num == 3:
#         pass  #do nothing for now
#     else:
#         print(num)


# Lets Try while loop again
# while True:
#     print("\nMenu")
#     print("1. Say Hello")
#     print("2. Say Goodbye")
#     print("3. Exit")

#     choice = input("Choose and option: ")

#     if choice == "1":
#         print("Hello")
#     elif choice == "2":
#         print("Goodbye")
#     elif choice  == "3":
#         print("Exiting program...")
#         break
#     else:
#         print("Invalid choice.Try again.")
        # break
    

# Try and use while True for validation
# while True:
#     age = input("Enter your age: ")
#     if age.isdigit():
#         print(f"Your age is {age}")
#     else:
#         print("Invalid input. Please enter a number.")
#     break

# num = 1
# while num <= 10:
#     print(num, end=" ")
#     num += 1

# timer = 10
# while timer > 0:
#     print("Countdown:", timer, end=" ")
#     timer -= 1

# for num in range(1,10):
#     if num == 5:
#         break
#     print(num)

for num in range(1,10):
    if num == 5:
        continue
    print(num)
