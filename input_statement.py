'''
#Basic usage of input()
name = input("Enter your name:")
print("Hello,", name)


#Convert using input
age = int(input("Emter your age: "))
print(f"You will be {age + 1}years old next year.")

#Calculator using input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum_reult = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_reult}")
'''


#1 - Request the name of the customer
#2 - greet the customer
#3 - request food preference
# 4- confirm receipt of order

name = input("What is your name?")
print(f"Hi {name}, Welcome to Hizzy Restaurant!")
food_order = input("What would you like to eat?")
print(f"Expect {food_order} in a minute! Thank you.")