# Task4 : Unique Members Registration

# request for name
names = input("Enter three names separated with comma: ")
# split names in the tuple
names_set = set(names.split(","))
names_set = set(name.strip() for name in names_set)
# make the length of each name be the value for each name
name_dict = {name: len(name) for name in names_set}
print(name_dict)