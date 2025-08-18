# String Operations Practice Question

# Task 1
# 1- Write a program to take string input from the user and display it in uppercase


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


# 8- Given a string with extra spaces, remove the leading and trailing spaces
request_char = input("Input a text of your choice with spaces both front and back:")
space_remover = request_char.strip()
print(space_remover)


# 9- ask the user to enter a sentence and print the number of  vowels in it
request_char = input("Enter any word of your choice:")
vowel_counter = request_char.lower()
print(vowel_counter.count("a") + vowel_counter.count("e")+vowel_counter.count("i")+vowel_counter.count("o")+vowel_counter.count("u"))




#10- Convert a string "123" to an integer and multiply it by 2

string_of_num = "1234"
string_splitter = (list(map(int, string_of_num)))
print(string_splitter)
# string_converter = string_splitter.split()
# string_converter
# print(string_converter)



# Task 3 : Pattern Matchin and Splitting
# 11-
#set variable
fruits = "apple,banana,orange"
# split list
print(fruits.split())


# 12- as the user for a sentence and print each word on a newline
# ask user for a new sentence
sentence_request = str(input("Hi there! Kindly enter a sentence:"))
# split the sentence into words
sentence_splitter = sentence_request.split()
# break each words into newline
sentence_breaker ="\n".join(sentence_request)
# print the words
print(sentence_breaker)



# 13-  Replace all spaces in a string with underscores(_)
sentence_request =str(input("Hi there! Enter sentence with spaces:"))
space_replacer = sentence_request.replace(" ", "_")
print(space_replacer)



# 14-  Count how many times the letter "a" appears in Banana
fruit = "Banana"
a_counter = fruit.count("a")
print(a_counter)

# 15- check if a given string start with "https://"
# request for url
get_url = input("Enter your url:")
# create url_checker
url_checker = get_url.startswith("https://")
# print if url start with https://
print(url_checker)
