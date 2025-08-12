'''
# Task 1
# Ask the user to input their fsvorite quote
quote_request = str(input("Hi! Enter your favourite quote:"))
# set case conversion
case_converter = quote_request.title()
# quotation_adder = case_converter.
print(f"'{case_converter}'") 


# Task 2: Shopping list Manager
# create empty list
cart_list =[]

# ask user to enter 3 shopping items
items_request_1 =input("Hello Customer, insert your first item: ")
items_request_2 =input("Hello Customer, insert your second item: ")
items_request_3 =input("Hello Customer, insert your third item: ")
# append items to cart
cart_list.append(items_request_1)
cart_list.append(items_request_2)
cart_list.append(items_request_3)
# print cart list
print(f"Dear customer, your items: {cart_list} are now added to cart. Thank you!")


# Task 3-  Word Counter
# ask user for a sentence

bag_of_words = input("Kindly insert a sentence: ")
# create words splitter
sentence_splitter = bag_of_words.split()
# count the words
word_counter = len(sentence_splitter)
print(word_counter)



# Task4: Name Organizer
# ask user to enter 5 names separatedby space
list_of_names = input("Input five names separatd by space: ")
# create case converter
case_converter = list_of_names.lower()
# sort the list
splitter = case_converter.split()
splitter.sort()
print(*splitter, sep="\n")


# Track 5: Student Score Tracker
# create two empty list
student_name = []
student_score =[]
# student name request
name_request_1 = input("Enter the first student name: ")
name_request_2 = input("Enter the second student name: ")
name_request_3 = input("Enter the third student name: ")

# request student score
score_request_1 = int(input("\nInput score for first student: "))
score_request_2 = int(input("Input score for first student: "))
score_request_3 = int(input("Input score for first student: "))

# append student name
student_name.append(name_request_1)
student_name.append(name_request_2)
student_name.append(name_request_3)

# append student scores
student_score.append(score_request_1)
student_score.append(score_request_2)
student_score.append(score_request_3)

print(f"\nName:{student_name}\nScore:{student_score}")


# Task6 : Word analyzer
word = []

# request word
word_request = input("Input a word: ")
# uppercase checker
word.append(word_request)
uppercase_checker = all(s.isupper() for s in word)
print(f"All in uppercase: {uppercase_checker}")
# lowercase_checker
lowercase_checker = all(s.islower() for s in word)
print(f"All in lowercase: {lowercase_checker}")

# Titlecase Checker
titlecase_checker = all(s.istitle() for s in word)
print(f"All in lowercase: {titlecase_checker}")
'''


# Task 7: List Maniputalation
# list city names
cities = ["Jalingo", "Ibadan", "Abeokuta", "Ikeja", "Bobape"]

# request city name
print(f"{cities} are the cities on the itinerary, change Abeokuta to any other city of your choice" )

# request for third city replacement
city_name_request = str(input("Enter a city of your choice: "))
# remove abeokuta
cities.remove("Abeokuta")
# insert new city
cities.insert(2, city_name_request)
# remove last city
cities.remove("Bobape")
# insert a new city at the beginning
cities.insert(0, "Abuja")
print(cities)





                                                                                                                                                                                                                          