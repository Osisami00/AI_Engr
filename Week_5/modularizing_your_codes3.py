<<<<<<< HEAD
# How attributes and methods work together

# attribute store data
# method use and modify that data

class BankAccount:
    def __init__(self, owner, bank_name, balance=0):
        # Attribute: WHat the account has
        self.owner = owner
        self.bank_name = bank_name
        self.balance = balance 
        self.account_number = self.generate_account_number()

    # METHOD - WHAT THE ACCOUNT CAN DO
    def deposit(self, amount):
        """Add money to the account"""
        if amount > 0:
            self.balance += amount  #methods changes attribute
            return f"#{amount:,} deposited to {self.owner}'s {self.bank_name} account. New balance: #{self.balance:,}"
        else:
            return "invalid deposit amount"
        
    def withraw(self,amount):
        """To remove money from the account"""
        if amount > 0 and amount <= self.balance:
            return f"#{amount:,} withrawn from {self.owner}'s account. New balance is {self.balance:,}"  
        return "Insufficient funds or invalid amount"   
       
    def transfer(self, amount, recipient):
        """To  transfer money to another account"""
        if amount < 0 and amount >= self.balance:
            return f"#{amount:,} transfered successfully to {recipient} . Your new balance is #{self.balance - amount}"
        return f"Transfer failed: insufficient funds"
    
    def check_balance(self):
        """Check Balance"""
        return f"{self.owner}'s {self.bank_name} account balnce: #{self.balance:,}"

    def generate_account_number(self):
        """GEenrate a unique account number"""
        import random
        return f"01{random.randint(10000000, 9999999999)}"
    


    # creating and using account
sammy_account = BankAccount("Sammy Olaiya", "Zenith Bank", 50000)


#Attributes (characteriistics)
# print(f"Owner: {sammy_account.owner}")
# print(f"Bank: {sammy_account.bank_name}")
# print(f"Account Number: {sammy_account.account_number}")


# Methods (actions)
print(sammy_account.check_balance())
print(sammy_account.deposit(100000000))
print(sammy_account.check_balance())
print(sammy_account.withraw(1000))
print(sammy_account.check_balance())
print(sammy_account.transfer(3000, "Tolu"))
print(sammy_account.check_balance)
=======
# WHAT IS INIT

# __init__ is a special method called a constructor) that automatically runs when you create 
# you create a new object. Think of it as the birth cerificate process - its
# sets up all the basic information about the new obj



# class Student:
#     def __init__(self, name, course, level):  #This runs automatically
#         print("Creating a new student...")
#         self.name = name
#         self.course = course
#         self.level = level
#         print(f"Student {name} has been crerated!")

# # when you create a stude, __init__ runs automatically
# kemi = Student("Kemi", "Computer Science", 300)
# kemi.name = input("Enter your name: ")

# print(kemi.name)


# How INIT and self work together

# class NigerianStudent:
#     def __init__(self, name, state, course):
#         print(f"Step 1: creating student object...")
#         self.name = name
#         self.state_of_origin = state 
#         self.course = course
#         self.student_id = self.generate_id()
#         print(f"Step 6: {self.name} from {self.state_of_origin}, is ready")

#     def generate_id(self):
#         import random 
#         return f"UNISAIL{random.randint(1000,9999)}"

# Michael = NigerianStudent("Michael", "Lagos", "Ai_Engr")
# print(Michael.name)
# print(Michael.student_id)


class PhoneUser:
    def __init__(self, name, network):
        self.name = name
        self.network = network
        self.airtime = 0
        print(f"{self.name} joined {self.network} network")

    def buy_airtime(self, amount):
        self.airtime += amount   #self ensures it goes ton the RIGHT PERSON
        return f"{self.name} now has #{self.airtime} airtime"
    
# creatingmultiple USers
abeeb = PhoneUser("Abeeb Ada", "Airtel")
della = PhoneUser("Della Rae", "MTN")


# eACH PERSONS actions affect only their own account
print(abeeb.buy_airtime(500))          #Abeeb now has 500 airtime
print(della.buy_airtime(3000))         #della now has 3k airtime
print(abeeb.airtime)
print(della.airtime)



# ATTRIBUTES
# Attribute are the characteristics, properties, or data that 
# describe an object. They answer the question "What does this obj "
# "looks like" or "What info does the object store"
>>>>>>> 5c30e069ad7672e04077858c29e276a3e1b5f8b1
