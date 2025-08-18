# Python Operators
'''
# Operators are special symbols in python that performs operations on 
# on variables and values. Here we will focus on;
# 1- Comparison Operators
# 2- Assignment Operators
# 3- Logical Operators

# # COMPARISON OPERATORS
#     -comparison operators are used to comapare two values.
# The result is always True or False

a = 10
b = 20
print(a == b)  #False

print(a != b) #True

print(a >= 10) #True

print(b <= 25)  #True

# USe case Example- Student Exam Result
score = 75

print(score >= 50) #True(passed)
print(score <= 50)  #False (Failed)
print(score == 100)  #False


# ASSIGNMENT OPERATORS
# assignment operators are used to assign values to variables 
# they can also combine an operation with assignment,
# so instead of writing x = x + 5 we can write x+=5

# x =10 
# print("Initial value: ", x)


# x += 5
# print("After x += 5:", x)

# x -= 2
# print("After x-= 2:", x)

# x *= 3
# print("After x  *3:", x)

# x /= 5
# print("After x /= 4:", x)

# x %= 3
# print("After x %= 3:", x)

# Use Case Examples
# Define Variables

balance = 1000
deposit = 200
withdraw = 150

balance += deposit  #add deposit =1200
balance -= withdraw # subtract withdrawal = 1050
print("Updated Balance:", balance)

# LOGICAL OPERATORS
# Logical operators are used to combine conditional statements
# They work with Boolean values (True/False)
x =10 
y = 20

# AND OPERATOR
print(x >5 and y > 15)  #True

# OR OPERATOR
print(x < 5 or y > 15)  #True 

# NOT OPERATOR
print(not(x == 10))  #false
'''

# Use Case Example 1: Scholarship Eligibility

# Define variables
age = 17
score = 85

# must be younger than 18 and score above 80

eligible = (age < 18) and (score > 80)  #False
print("Scholarship Eligibility:", eligible)



# Use Case2 - Event Access
age = 22
has_ticket = False

can_enter = (age >= 18) and (has_ticket or age < 25)