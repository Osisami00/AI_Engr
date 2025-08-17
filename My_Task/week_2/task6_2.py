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
# print names of antendants
print(attendee_names_set)