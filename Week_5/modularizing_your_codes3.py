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