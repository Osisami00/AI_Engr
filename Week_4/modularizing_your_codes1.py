'''
# Built-in Funcs
#range()

# for i in range(3):
#     print(i)  #0,1,2


# # zip()
# names = ["Esther", "Precious", "Kenny"]
# scores = [85, 90, 75]
# for n, s in zip(names, scores):
#     print(n, "scored", s)


# map() and lambda
# nums = [1,2,3,4]
# squared = list(map(lambda x: x**2, nums))
# print(squared)  #[1, 4, 9, 16]

# # filter()
# even_num = list(filter(lambda x: x % 2 == 0, nums))
# print(even_num)  #[2,4]


# Student Performance & Feedback System

# Step 1: Input student data
name1 = input("Enter first student name: ")
score1 = int(input("Enter score for " + name1 + ": "))

name2 = input("Enter second student name: ")
score2 = int(input("Enter score for " + name2 + ": "))

name3 = input("Enter third student name: ")
score3 = int(input("Enter score for " + name3 + ": "))

# Step 2: Store in lists
names = [name1, name2, name3]
scores = [score1, score2, score3]

# Step 3: Display data
print("\nStudent Data:")
for index, (n, s) in enumerate(zip(names, scores)):
    print(f"{index + 1}. {n} - {s}")

total = sum(scores)
average = round(total /len(scores), 2)
highest = max(scores)
lowest = min(scores)

# print("\nPerformance Summary:")
# print("Total Score:", total)
# print("Average Score:", average)
# print("Highest Score:", highest)
# print("Lowest Score:", lowest)

# Step 5: Ranking (using sorted and zip)
ranked = sorted(zip(scores, names), reverse =True)
# print(ranked)
print("\nRanking:")
for rank, (score, name) in enumerate(ranked, 1):
    print(f"{rank}. {name} - {score}")


# # Step 6: Check data types
# print("\nData Type Checks:")
# print("Type of names:", type(names))
# print("Type of scores:", type(scores))
# print("ID of names list:", id(names))
# print("ID of scores list:", id(scores))


# Step 7: Filter passing students (>=50)
# passing = list(filter(lambda x: x >= 50, scores))
# print("\nPaasing Scores:", passing)

# Step 8: Map names to uppercase
uppername = list(map(lambda x: x.upper(), names))
print("\nNames in Uppercase:", uppername)

# Step 9: Use help() to show documentation of len
print("\nHelp on len():")
help(len)



# USER DEFINED FUNCTION
# Defining a function
def greet():
    print("Hello, welcome to AI Fellowship!")

# When you want to use a function, this is how to call it.
# And you can call it as many times as possible.
greet()
greet()
greet()

#Funcs and Args and Params
# - Arguements are variables yoiu add inside the func parenthesis
#  - Param are actual values you pass inside the func parenthesis

#FUNCs with an arg - the plaaceholder
def greet(name):
    print("Hello", name, "welcome to python learning")

#Calling with param - the actual name
greet("Class rep")


# When to use return, print(), yield keywords inside a func
# a. print()
#  - You can use it if you just want to display your output(NOT STORING). 
# iT Doesnt give backa value you can use later

# def greet(name):
#     print("Hello", name)

# # Function call
# result = greet("Esther")

# # You will notice that it did not store the name
# print("Result:", result)


# B. RETURN
#   - You can use it when you wanto give back a value
    # -Return sends a value back to to the func caller

# Example
def add(a,b):
    return a+b

result = add(4,6)
print("The sum is ", result)


# C. YIELD
# This is used for producing a sequence (Generators)
    # -Yeld works like return, instead of ending the func, it pause it and
# remembers its states
# Next time you call it, it resumes from where it stopped
# This creates a generator
# You can usew it when working with large data or infinite sequences

def count_up_to(n):
    i = 1
    while i < n:
        yield i
        i += 1
# using the generator
for number in count_up_to(5):
    print(number)



# MORE ON FUNCS ARGS (types of arg)
# func can accept different types of args depending on how we 3want to pass data

#  1- Positional Args
# These are the most common
# The order matters: values are assigned to param in the same order as they appear
# Think of it like being up 

def introduce(name, track): 
    print("My name is ", name)
    print("I am learning", track, ".")
introduce("Michael", "AI Engineering")


# 2- Keyword Args - kwargs
# Here, you explicitly mention the param name when calling the func
def introduce(name, track):
    print("My name is", name)
    print("I am learning", track,".")

# function call
introduce(name = "Ngozi", track = "AI Engineering")

# Change the arrangment and watch the output

introduce(track = "AI Engineering",name = "Ngozi")   # HEre you notice that order does not batter


# DEFAULT ARGs
# Here, you can give param a default value
# Even if there is no value provided, the default is used
# Think of it like a restruant menu where rice is served by default if you dont choose otherwise
def introduce(name, track = "AI Engineering"):
    print("My name is", name)
    print("I am learning", track, ".")

# function call
# Without specifying the default argument, but watch the ouput
introduce("Paul")  
# Specify the default argument and watch the output

introduce("Tunji Paul", track = "AI Development")


# 4- Verying Length Arg
# a - non-keyword (tuple)
# collect extra positional arguement into tuple
# Think of it like packing extra clothes into a bag

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Sum", total)

add_numbers(2,4,6)
add_numbers(10,20,30,40,50)


# keyword arg (dict)
# collects extra keyword arguement into dict


def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_details(name="Peter", track = "AI Engineering", interest="Block Chain")



# Let's implement on full code
def participant_profile(name, age, track="AI Engineering", *skills, **extra_info):
    """
    Generate a profile for a bootcamp participant using different types of arguments.
    """
    profile = f"\n ---- Bootcamp Participant Profile ----\n"
    profile += f"Name: {name}\n"
    profile += f"Age: {age}\n"
    profile += f"Track: {track}\n"

    #skills (from *args)
    if skills:
        profile += "Skills: " + ", ".join(skills) + "\n"
    else:
        profile += "Skills: Not yet specified\n"
    
    # Extra Info (from **kwargs)
    if extra_info:
        profile += "Additional Info:\n"
        for key, value in extra_info.items():
            profile += f" - {key.capitalize()}: {value}\n"

    return profile 

# ---------- LEts test ----------

# Example 1: Using only positional arguments
# print(participant_profile("Michael", 24))

# Example 2: Adding keyword/default argument
# print(participant_profile("Ridwan", 29, track="AI Developer"))

# Example 3: Adding variable-length positional arguments (*args)
# print(participant_profile("David", 27, "Data Science", "Python", "SQL", "Machine Learning"))

# Example 4: Adding variable-length keyword arguments (**kwargs)

print(participant_profile(
    "Sophia", 30, "Cybersecurity",
    "Networking", "Ethical Hacking", "Python",
    interest="Blockchain", city="Shagamu", phone="08123456789"
))
'''


# Namespaces and Scope
# Namespace and Scope