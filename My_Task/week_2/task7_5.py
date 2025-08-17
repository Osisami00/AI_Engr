# Task 5: Contact Quick Lookup
names = ("Michael", "Damilola", "Temmy")
phone_num = (123,345,678)
info = {name: num for name, num in zip(names, phone_num)}

# request name
user_name = input("Enter a name: ")
print(info.get(user_name))