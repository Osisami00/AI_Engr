# Tuple Practice
'''

# Task1: Create and Display
nigerian_dishes = []

# ask users for Nigerian dishes

dish_request1 = input("Hi there! Enter your first Nigerian dish: ")
dish_request2 = input("Hi there! Enter your second Nigerian dish: ")
dish_request3 = input("Hi there! Enter your third Nigerian dish: ")

# create list to append dishes
nigerian_dishes.append(dish_request1)
nigerian_dishes.append(dish_request2)
nigerian_dishes.append(dish_request3)
# convert list to tuple
nigerian_dishes_tuple = tuple(nigerian_dishes)
print(*nigerian_dishes_tuple, sep="\n")





# Task2 : Tuple and Input
# create an empty list
best_friends_list = []
# request names of best friends
name_request1 = input("Hi there! Enter your first best friend: ")
name_request2 = input("Hi there! Enter your second best friend: ")
name_request3 = input("Hi there! Enter your third best friend: ")
name_request4 = input("Hi there! Enter your fourth best friend: ")
name_request5 = input("Hi there! Enter your fifth best friend: ")
# append names to list
best_friends_list.append(name_request1)
best_friends_list.append(name_request2)
best_friends_list.append(name_request3)
best_friends_list.append(name_request4)
best_friends_list.append(name_request5)
tuple_friends = tuple(best_friends_list[::-1])
print(tuple_friends)


# Task3: Tuple Operations
# create an empty list
# nigeria = []
# request names of  Nigerian state
name_request =(
    input("Hi there! Enter your first Nigerian state: "),
    input("Hi there! Enter your second igerian state: "),
    input("Hi there! Enter your third  Nigerian state: "),
    input("Hi there! Enter your fourth  Nigerian state: "),
    input("Hi there! Enter your fifth  Nigerian state: ")
)

print(f"Your first state is {name_request[0]}")
print(f"Your last state is {name_request[-1]}")
print("Lagos" in name_request)
name_length = len(name_request)
print(f"The number of states you entered is {name_length}")


# Task 4: tuple Unpacking
# Request Biodata

tuple_profile = (
    input("Hi there! Enter your first name: "),
    input("Hi there! Enter your age: "),
    input("Hi there! Enter your favorite color: "),
    input("Hi there! Enter your hometown: ")
)


# unpack biodata
first_name, age, favorite_color, home_town = tuple_profile
print(f"Here is your bio-data:\nName: {first_name}\nAge: {age}\nFavorite Color: {favorite_color}\nHometown: {home_town}")
'''

# Task 5: Modify Tuple Indirectly
my_cart = (
    input("Hi there! Enter your first item: "),
    input("Hi there! Enter your second item: "),
    input("Hi there! Enter your third item: ")
)
# List Converter
list_converter = list(my_cart)
list_converter.append(input("Enter one extra item: ")),
list_converter.append(input("Enter your last item: "))

my_cart_tuple = tuple(list_converter)
print("|".join(my_cart_tuple))



# Task6:  Attendance Tracker
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November" "December")

student_bio = (
    input("Enter your name: ")
    input("Are you Male and Female? ")
    input("Enter course track: ")
    input("Enter current month number: ")
    input("Enter current day number: ")
)

day = days[[days] + 1]
month = months[[months] + 1] 

