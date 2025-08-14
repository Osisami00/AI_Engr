# PYTHON DICTIONARY
    #-A dictionary in python is a collection of key-values
    # -Values can be any data types(string, int, list, tuple,even another dict)

# syntax 
# dict_name = {key1: value1, key2: value2}

# Features
#-5 Key-value structure
#4- Mutable
#3-  Unordered (before Python 3.7): from pyhton 3.7+, they maintain insertion order
#2- Unique keys
#1-  keys must be immutable

'''
# CREATING DICTIONARIES
# 1- Using curly braces
student = {
    "name": "Ada",
    "age": 20,
    "course": "Computer Science"
}
print(student)

# 2- Using the dict() constructor
student_info = dict(name="John", age=25, course="MAths")
print(student_info)

# 3- Empty dictionar
empty_dict = {}
print(empty_dict)

# Dictionary Comprehension
# Syntax: {key_expression: value_expression for item in iterable if condition}

#1- Create a dictionary of number and their squares
squares = {x:x**2 for x in range(1,6)}
print(squares)

#2-  With Conditions
# Dictionary of even numbers and their cube
even_cube = {x:x**3 for x in range(6) if x % 2 ==0}
print(squares)

#3- From Existing 
students = {
    "name": 85,
    "John": 40,
    "Musa": 65
}

# Filter Student who passed (Score>=50)
passed_students = {name:score for name, score in students.items( )if score>=50}
print(passed_students)

# 4- Using String Keys
names = ["Ada", "john", "Musa"]
lengths = {name: len(name) for name in names}
print(lengths)

# Accessing Dictionsry Items
# Define  a dictionary
student = {
    "name": "Ada",
    "age": 20,
    "course": "Computer Science"
}
#1-  Using kEY
print(student["name"])

# 2- Using get() method

print(student.get("age"))
print(student.get("grade"))  #Not found



# MODIFYING ITEMS GROM DICTIONARIES

# 1- USING pop()
# student.pop("course")
# print(student)

# 2- Using popitem() - removes last inserted key-value
# student.popitem()

# 3- Using del keyword
# del student["course"]

# 4- using clear() - removes all items
# students.clear()
# print(student)


# DICTIONARY METHODS
person = {"name": "Emeka", "age":30}

# 1- .keys()
print(person.keys())

# 2- Values()
print(person.values())

# 3- .items()
print(person.items())

# 4- .update()
person.update({"age": 31, "city": "Lagos"})
print(person)


# NESTED DICTIONARIES
students = {
    "student1": {"name": "Ada", "age":20},
    "student2" : {"name":"John", "age": 30}
}
print(students["student1"]["name"])
'''


#Loop through Keys
student = {
    "name": "Ada",
    "age": 20,
    "course": "Computer Science"
}
# for key in student:
#     print(key)

# # Loop through values
# for value in student.values():
#     print(value)

# for key,value in student.items():
#     print(f"{key} : {value}")

# Storing a student's biodata
student = {
    "name": "Chinedu",
    "age": 19,
    "department": "Engineering",
    "subjects": ["Maths", "Physics", "Chemistry"],
    "is_full_time": True
}

print(f"Name: {student['name']}")
print(f"Subjects: {'| '.join(student['subjects'])}")