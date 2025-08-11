# String Operations Practice Question

# Task 1
# 1- Write a program to take string input from the user and display it in uppercase

'''
#  ask for username
name = str(input("What is your name?"))
print(name.upper())

# 2- Given the string "python", print its first and last characters
# set pyhton variable
name = "python"
first_char = name[0]
last_char = name[-1]
print(first_char, "and",  last_char)


# 3- Ask for the users name and print Hello,! where the user's input
#ask for user's name
name = str(input("What is your name?"))
print(f"Hello! where is the user's input, {name}?")


#4 Write a program to count the number of character in a string

character = input("Input a character:")
character_length = character.find(character[-1]) + 1
print(character_length)


#5 Give Hello World, replace world with Python
greeting = "Hello World"
print(greeting.replace("World", "Python"))



# Task 2
# 6- Check if a given string is a substring "python"
request_char = input("Input a text of your choice:")
python_substring = request_char in "python"
print(python_substring)


# 7- Write a program thatv reverse a string without using slicing
request_char = input("Input a text of your choice:")
char_reverse = "".join(reversed(request_char))
print(char_reverse)
'''

# 8- Given a string with extra spaces, remove the leading and trailing spaces
request_char = input("Input a text of your choice with spaces both front and back:")
space_remover = request_char.strip()
print(space_remover)
