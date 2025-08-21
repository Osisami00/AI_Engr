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