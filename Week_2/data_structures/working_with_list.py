# Data Dtructure: A list of python is an orderded, mutable 
#How to creat a List

# 1- You can create an empty list when you dont have elements but you plan to add later

# Method 1 - using squared brackets
empty_list = []
print(empty_list)

# Method 2: Using the lsit() constructor
empty_list2 = list()
print(empty_list2)

# 2- Creating a list with initial Element
        # -list can store multiple items with comma sepearitg them
# List of Integers
numbers = [1,2,3,4,5]
print(numbers)

# List of Strings
fruits = ["apple", "banana", "cherry"]
print(fruits)


# Mixed Data types
mixed_list = ["Alice", 25, 5.8, True]
print(mixed_list)


# 3- Creating a List from Another Sequence. You can convert strings, tuples or other iterables into a list
#from a string (each character becomes an element)

chars = list("hello")
print(chars)

#from tuple
my_tuple =(10,20,30)
list_from_tuple = list(my_tuple)
print(list_from_tuple) 

# from range
number_range = list(range(5))
print(number_range)

# 4. Creating a list usinh comprehension. List comprehensions are a concise way to
# create list using a loop in oine line. 

#Squares of number 0-4
squares = [x**2 for x in range(5)]
print(squares)

# Even number between 0-10
evens =[x for x in range(11) if x % 2 == 0]
print(evens)

# Creating a Nested List. A list can contain other lists. It is useful for matrices or grouped data
# Matrix-Like list
matrix = [[1,2],[3,4],[5,6]]
print(matrix)

#Accesing element in a nested list
print(matrix[0])
print(matrix[1])
print(matrix[0][1])
print(matrix[2][1])

# Characteristics of A List
# 1- Ordered Collection
#  - The elements in a list maintain the order in which they are inserted
#    - The first element has index 0, the second has 1

fruits = ["mango", "orange", "banana"]
print(fruits)
print(fruits[0])
print(fruits[2])

# 2 - Allows Duplicates
# Lists can store the same value multiple times
items = ["rice", "beans", "yam", "rice"]
print(items)

# 3- Mutable (Can be changed)
    # -You can modify a list after it is crated - change, append, or remove existing ones

numbers = [1,2,3]
numbers[1] = 20
print(numbers)


# 4- Can contain Different Data Types
    # -A list can hold int, str,fl, bool, and even other lists
mixed = [10, "Nigeria", 3.14,True]
print(mixed)

# 5- Can be Nested
    # -A list can contain other list(2D or multi-dimensional)
nested_list = [[1,2],[3,4],["a","b"]]
print(nested_list)
print(nested_list[2][1])

#6 - Dynamic Size
    # -you dont need to declare the size of a list before hand; it can grow or shrink as needed
names = ["Ada", "ola"]
names.append("Bola")
names.append("Chidi")
names.remove("Ada")
print(names)
# name_remover = names.remove(names[0])
# print(name_remover)