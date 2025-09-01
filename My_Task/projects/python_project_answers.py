# BASIC CALCULATOR

# thought outline
# - Define function
# -wrap each function in while Loop
# -Add error handling
# -collect data 

# create a USSD code that request dialing *223#
# Ask users to choose between options
# Ask user end calculator if all enquiry has been responded



# 
# Addition Function
def add():
    try:
        while True:
            number1 = input("Enter first number: ").strip()
            number2 = input("Enter second number: ").strip()
            if number1.isalpha() or number2.isalpha():
                print("Your entry cannot be a letter. Try again.")
                continue
            elif number1  =="1" and number2 == "":
                print("Error! You need to enter a number")
                continue
            else: 
                result = float(number1) + float(number2)
                print(f"Result: {result}")
            break
    except ValueError as e:
        print("You need to enter a number.")
    

# Subtraction Function
def subtract(): 
    try:
        while True:
            number1 = input("Enter first number: ").strip()
            number2 = input("Enter second number: ").strip()
            if number1.isalpha() or number2.isalpha():
                print("Your entry cannot be a letter. Try again.")
                continue
            elif number1  =="" and number2 == "":
                print("Error! You need to enter a number")
                continue
            else: 
                result = float(number1) - float(number2)
                print(f"Result: {result}")
            break
    except ValueError as e:
        print("You need to enter a number.")





# Multuiplication Func
def multiply(): 
    try:
        while True:
            number1 = input("Enter first number: ").strip()
            number2 = input("Enter second number: ").strip()
            if number1.isalpha() or number2.isalpha():
                print("Your entry cannot be a letter. Try again.")
                continue
            if number1  =="" and number2 == "":
                print("Error! You need to enter a number")
                continue
            else: 
                result = float(number1) * float(number2)
                print(f"Result: {result}")
            break
    except ValueError:
        print("You need to enter a valid number (can include decimals).")







# Division Function
def divide(): 
    try:
        while True:
            number1 = input("Enter first number: ").strip()
            number2 = input("Enter second number: ").strip()
            if number1.isalpha() or number2.isalpha():
                print("Your entry cannot be a letter. Try again.")
                continue
            elif number1  =="" and number2 == "":
                print("Error! You need to enter a number")
                continue
            elif number1 == 0 or number2 == 0:
                print("Zero cannot be divided")
            else: 
                result = float(number1) / float(number2)
                print(f"Result: {result}")
            break
    except ValueError:
        print("You need to enter a valid number (can include decimals).")
    except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")




# Modulo 
def modulo(): 
    try:
        while True:
            number1 = input("Enter first number: ").strip()
            number2 = input("Enter second number: ").strip()
            if number1.isalpha() or number2.isalpha():
                print("Your entry cannot be a letter. Try again.")
                continue
            elif number1  =="" and number2 == "":
                print("Error! You need to enter a number")
                continue
            elif number1 == 0 or number2 == 0:
                print("Zero cannot be divided")
            else: 
                result = float(number1) % float(number2)
                print(f"Result: {result}")
            break
    except ValueError:
        print("You need to enter a valid number (can include decimals).")
    except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")



# Exponential
def exponent(): 
    try:
        while True:
            number1 = input("Enter first number: ").strip()
            number2 = input("Enter second number: ").strip()
            if number1.isalpha() or number2.isalpha():
                print("Your entry cannot be a letter. Try again.")
                continue
            elif number1  =="" and number2 == "":
                print("Error! You need to enter a number")
                continue
            elif number1 == 0 or number2 == 0:
                print("Zero cannot be divided")
            else: 
                result = float(number1) ** float(number2)
                print(f"Result: {result}")
            break
    except ValueError:
        print("You need to enter a valid number (can include decimals).")
    except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")
        

# exponent()
# add()
# multiply() 
# subtract()
# divide()
# modulo()



print("\nDear user, kindly dial *223# to use MOsiPy Calculator.")
while True:
    try:
        code_request = input("\nEnter dial code: ").strip()
        if code_request == "*223#":
            print("\n <-----Successful----->\n")
            print("Welcome to MOsiPy calculator\nChoose one of the following options")
            break
        elif code_request == "":
            print("Error: Entry cannot be empty! Please dial *223#")
        else:
            print("Incorrect code! Please dial *223#")
    except TypeError:
        print("Error: Please dail *223#")
        # break

while True:
    try:
        
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Modulus")
        print("5. Division")
        print("6. Exponential")
        print("7. Exit MOsiPy Calculator")
        choice = input("\nEnter your choice of service: \n").strip()
        if choice == "1":
            print("\n")
            add()
        elif choice == "2":
            print("\n")
            subtract()
        elif choice == "3":
            print("\n")
            multiply()
        elif choice == "4":
            print("\n")
            modulo()
        elif choice == "5":
            print("\n")
            divide()
        elif choice == "6":
            print("\n")
            exponent()
        elif choice == "7":
            print("Thank you for using MOsiPy Calculator")
            break
        elif choice != "1" or "2" or "3" or "4" or "5" or "6" or "7":
            print("Wrong input. Enter between 1-7 in the prompt")
        elif choice == "":
            print("Entry can not be empty")
        if choice == "7":
            print("Thank you for using MOsiPy Calculator")
            break
    except TypeError:
        print("Error: Please dail *223#")
        break