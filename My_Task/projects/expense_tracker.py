# @title 17. Basic Expense Tracker
"""
An Expense Tracker is a practical application that
allows users to log their daily expenses and track spending
habits. This project enhances knowledge of file handling,
data storage, and user input processing in Python.
This chapter covers the step-by-step implementation of an
Expense Tracker, including user input handling, data storage
in a CSV file, and displaying expense reports.

Key Concepts of Expense Tracker in Python

Data Handling:

Using lists and dictionaries to store
expenses
Writing and reading data from a CSV file

User Input Processing:

Taking user input for expense details
Validating and formatting input data

Report Generation:

Displaying total expenses per category
Summarizing daily or monthly spending

"""

# thoughts process
# 1. get item list and prices
# 2. give sum total of expenses
# 3. deduct expenses from balance
# 4. print if person account balance is okay

balance = 10,000

def expense_tracker():
    expenses={}
    try:      
        while True:
            item1 = input("Enter first item: ").strip()
            if item1 =="":
                print("Item cannot empty")
                continue
            elif item1.isdigit():
                print("Item cannot be a number")
                continue
            else:
                pass
            price1 = int(input("Enter price of item: "))
            if price1 =="":
                print("Item cannot empty")
                continue
            elif price1.isalpha():
                print("Price cannot be a word")
                continue
            else:
                expenses["item1"] = int(price1)



            item2 = input("Enter second item: ").strip()
            if item2 =="":
                print("Item cannot empty")
                continue
            elif item2.isdigit():
                print("Item cannot be a number")
                continue
            else:
                pass 
            price2 = int(input("Enter price of item: "))
            if price2 =="":
                print("Item cannot empty")
                continue
            elif price2.isalpha():
                print("Price cannot be a word")
                continue
            else:
                expenses["item2"] = int(price2)


            item3 = input("Enter third item: ").strip()
            if item3 =="":
                print("Item cannot empty")
                continue
            elif item3.isdigit():
                print("Item cannot be a number")
                continue
            else:
                item3 = int(item3)
            price3 = int(input("Enter price of item: "))
            if price3 =="":
                print("Item cannot empty")
                continue
            elif price3.isalpha():
                print("Price cannot be a word")
                continue
            else:
                expenses["item3"] = int(price3)



            item4 = input("Enter fourth item: ").strip()
            if item4 =="":
                print("Item cannot empty")
                continue
            elif item4.isdigit():
                print("Item cannot be a number")
                continue
            else:
                item4 = int(item4)
            price4 = int(input("Enter price of item"))
            if price4 =="":
                print("Item cannot empty")
                continue
            elif price4.isalpha():
                print("Price cannot be a word")
                continue
            else:
                expenses["item4"] = int(price4)



            item5 = input("Enter fifth item: ").strip()
            if item5 =="":
                print("Item cannot empty")
                continue
            elif item5.isdigit():
                print("Item cannot be a number")
                continue
            else:
                pass
            price5 = int(input("Enter price of item"))
            if price5 =="":
                print("Item cannot empty")
                continue
            elif price5.isalpha():
                print("Price cannot be a word")
                continue
            else:
                expenses["item5"] = int(price5)


            # expenses["item5"] = int(price5)
            total_cost = expenses["item1"] + expenses["item2"]+ expenses["item3"] + expenses["item4"] +expenses["item5"]
            expenses = balance - total_cost
            if total_cost <= 1000:
                print("Your are running low on cash")
            elif total_cost >= 1000:
                print("You still have enough money on you!")
            else:
                print("You are broke bro!")
                break
            break
    except Exception as e:
        print("Error! wrong Entry", e)
        print(expenses)

expense_tracker()