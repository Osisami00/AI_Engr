# Tast 10: Error Handling 

# Simulated USSD Menu Interaction

print("Yello! Dial *556# for data and other services")

ussd_code = "*556#"
ussd_request = input("Yello! enter ussd code: ")

while ussd_request != ussd_code:
    print("You entered the wrong code.")
    ussd_request = input("Yello! enter ussd code: ")

    



balance = 500   
airtime = []
data_amount = []



print("Yello Customer! What would you like to do today: ")
print("1. Check Balance")
print("2. Buy Airtime")
print("3. Buy Data")

ussd_request = input("Enter a number: ")
user_name = input("Kindly sign-up before using our service.\nEnter your name: ")
phone_num = int(input("Enter your phone number: "))
password_request = input("Enter password: ")

print(f"\n\nYello Customer! What would you like to do today: ")
print("1. Check Balance")
print("2. Buy Airtime")
print("3. Buy Data")

try:
    if ussd_request == "1": 
        print(f"Your balance is {balance}.")
    elif ussd_request == "2":
        airtime =input("How much airtime do you want to buy: ")
        print(f"Your airtime purchase of #{airtime} is succesful")
    elif ussd_request =="3":
        data_amount = int(input("How much data do you want: "))
        if data_amount >= balance :
            print(f"Insufficient Balace. Your available balance is #{balance}. Buy #{data_amount-balance} airtime to buy #{data_amount} data.")
        else:
            print(f"✅Data bought successfully!")
    else: 
        print("Enter a valid number.")
except ValueError:
    print("Your input must be a number.")