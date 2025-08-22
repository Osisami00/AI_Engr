# Simulated USSD Menu Interaction

balance = 500
airtime = []
data_amount = []

name = input

print("Yello Customer! What would you like to do today: ")
print("1. Check Balance")
print("2. Buy Airtime")
print("3. Buy Data")

ussd_request = input("Enter a number: ")

if ussd_request == "1": 
    print(f"Your balance is {balance}.")
elif ussd_request == "2":
    airtime =input("How much airtime do you want to buy: ")
    print(f"Your airtime purchase of #{airtime} is succesful")
elif ussd_request =="3":
    data_amount = int(input("How data do you want: "))
    if data_amount >= balance :
        print(f"Insufficient Balace. Your available balance is #{balance}. Buy #{data_amount-balance} airtime to buy #{data_amount} data.")
    else:
        print(f"Data bought successfully!")
else: 
    print("Enter a valid number.")


# Task6-Question 3 - Football Match System
# **Task3: Simulate a football match ticket system**

# - Store all seat numbers (1 to 50) in a set.

# - Ask users to "book" a seat by entering the number.

# - Remove booked seats from the set.

# - Show remaining seats after each booking.

print("Dial *222# to book a football ticket")
dial_code = "*222#"
dial_code_request =input("Enter ticket dial code: ")

while dial_code_request != dial_code:
    dial_code_request = input("Enter ticket dial code: ")
    

ticket_number = range(1,50)
booking_request = int(input("Book a seat number: "))

while True: 
    if booking_request in ticket_number:
        print(f"Your ticket book is succesful!")  
    else: 
        print("Invalid number. Choose a number between 1-50")
    break


# Task6 -Question 4: Unique Voters Registration
# - Ask for voter names and store in a set.

# - If a voter tries to register twice, display a warning.

# - After registration, display the total number of unique voters.
