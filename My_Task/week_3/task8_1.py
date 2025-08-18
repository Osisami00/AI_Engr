# Task 1 
# Explain each output of the program below:
# Give 3 use cases or scenarios where you can apply the program
# Write the program for 1 


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
# 3- Result checker


# Market Budget
# request price for first item
rice = float(input("Enter amount of money you budget for Rice: "))
beans = float(input("Enter the amount of money you budget for beans: "))

print(f"{rice} > {beans} : {rice > beans}")
