# Tuples
# - Atuple is an ordered, immutable (unchangeable) collection of items in python


# Creating Tuples

# 1- using parentheses
fruits = ("apple", "banana", "cherry")
print(fruits)

# 2- Without parenthese (tuple packing)
numbers = 1,2,3
print(numbers)

# 3- Single-item tuple (must include a comma)
single_item = ("apple",)
print(single_item)
print(type(single_item))

# using the tuple() constructor
fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits_list)


# Characteristics of Tuples
# 1- Ordered - items have a fixed position
colors = ("red", "green", "blue")
print(colors[0])

# 2- immutable - cannot change after creation
# colors[1] = "yellow"  #error

# 3- Allow duplicates - same value can appear multiple times
numbers = (1,2,3,3)
print(numbers)

# 4- Mixed Datatypes
mixed = ("apple", 3, True, 5.6)
print(mixed)


# Nexted tuple 
nested = (("a", "b"), (1,2))
print(nested)
print(nested[0][1])

# TUPLE OPERATIONS
# Even though tuples are immutabl, you can still perform several op

# 1- indexing
nested = (("a", "b"), (1,2))
print(nested)
print(nested[0][1])

# 2- slicing
fruits = ("apple", "banana", "cherry")
print(fruits[0:2])
print(fruits[::-1]) #turn backwards

# 3- concatenation
tuple1 = (1,2)
tuple2 = (3,4)
result = tuple1 + tuple2 
print(result)


# Repetition
nums = (1, 2)
print(nums * 2) #(1,2,1,2,1,2)


# Membership
fruits = ("apple", "banana", "cherry")
print("banana" in fruits)


#Iteration
for fruit in fruits: 
    print(fruit)

# Working with Tuples
# - You cant modify a tuple directly, but you:
    # 1- convert it to a list, modify then convert it back
    # 2- Use built in func to work with tuple contents


# 1- Unpackinf Tuples
person = ("john", 25, "Nigeria")
name, age, country = person
print(name, age, country)

# Tuple Methods
# Tuple has only two methods

# Count()
numbers = (1,2,3,4,5,5)
print(numbers.count(2))
print(numbers.count(5)) #counts number of occurences

print(numbers.index(3)) #positon of the first occurence of 3


# Converting between List and Tuple
# Tupel to list
t = (1,2,3)
list = list(t)
list.append(4)
print(list)

# List back Tuple
t =  tuple(list)
print = t


# Built in Functions with Tuples

list_of_numbs = (4, 1, 7, 3)
# print(len(numbs))
print(max(list_of_numbs))
print(min(list_of_numbs))
print(sum(list_of_numbs))

