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
    

# ticket_number = set(range(1,50))
ticket_number = set([i for i in range(1,51)])
booking_request = int(input("Book a seat number from 1-50: "))

while True: 
    if booking_request in ticket_number:
        print(f"Your ticket is booked succesful!")
        break
    else: 
        booking_request = int(input("Book a seat numbe 1-50: ")) 
    
unbooked_number_request = int(input("Enter 1 to check available seat numbers: "))
ticket_number.remove(unbooked_number_request)
while unbooked_number_request == 1:
    print("The available seat numbers are: ", ticket_number, sep=",")
    print("Good Bye!")
    break
else: 
    unbooked_number_request = int(input("Enter 1 to check available number: "))

