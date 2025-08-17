

# Task2: Unique Name Collector

# attendee_names =[]
# for attendee in range(5):
#     attendee =input("Hi! Kindly enter your name: ")
#     attendee_names.append(attendee)
# sorted_names = attendee_names.sort()
# print(sorted_names 

# Task2: uniques Name Collector
# create empty list
attendee_names =[]
# collect unique name
attendee1 = input("Enter your name: ")
attendee2 = input("Enter your name: ")
attendee3 = input("Enter your name: ")
attendee4 = input("Enter your name: ")
attendee5 = input("Enter your name: ")
# Append names to empty list
attendee_names.append(attendee1)
attendee_names.append(attendee2)
attendee_names.append(attendee3)
attendee_names.append(attendee4)
attendee_names.append(attendee5)
# sort and covert data to set
sorted_names = sorted(list(attendee_names))
attendee_names_set = set(sorted_names)

print(attendee_names_set)


# Task3: Football Match Ticket
seat_num = set([i for i in range(1,51)])
# ask user to book a seat
seat_num_request = int(input("Enter your seat number: "))
seat_num.remove(seat_num_request)
print(seat_num)
'''
# Task4 : Voters Registration System
voters_name = {"Ada", "Temmy", "Ella"}
# ask for voters name
request_name = input("Enter your name: ")
if request_name in voters_name:
    print("Voter already axist!")
else:
    print("Successful")


