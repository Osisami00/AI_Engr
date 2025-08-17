# Task3: Football Match Ticket
seat_num = set([i for i in range(1,51)])
# ask user to book a seat
seat_num_request = int(input("Enter your seat number: "))
# remove entered seat number from seat number
seat_num.remove(seat_num_request)
# print remaining seat number
print(seat_num)