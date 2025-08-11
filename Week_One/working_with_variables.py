#fworking with varibles
full_name = "Michael Damilola" #strings
age = 12  #int
male = True  #boolean
height = 12.7 #floats

# print(f"Your name is, {full_name}., You are {age} years old, a {male})
      
# TYPE CASTING
int_age = int(age)
# print()
# float()
# str()
# bool()

# Converting str to int
# age = int(input("Enter your age:"))
# print(f"you will be  {age + 1}years old next year.")

'''
# Calculator using input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_result}.")
'''
# 1- Input airtime no
# 2- Success, buy data
# 3- how many gig
# 4- for how long
# 5- auto-renew?


airtime_no = int(input("enter your voucher number"))
data_request = bool(input(("Do you want to buy data?")))
num_gig = float(input("How many gig do you want?"))
duration = int(input("How many weeks should your data last?"))
auto_renewal = bool(input("Do you want to renew your data?"))
print(f"Your {num_gig} gig subscription for {duration} weeks is Successfully!")