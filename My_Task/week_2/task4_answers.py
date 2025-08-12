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
sorter = case_converter.split()
# create splitter
sorter.sort()
print(*sorter, sep="\n")
'''

# Track 5: Student Score Tracker
name_request_1 = input("Enter the first student name: ")
name_request_2 = input("Enter the second student name: ")
name_request_3 = input("Enter the third student name: ")
# request student score
score_request_1 = int("Input score for first student: ")
score_request_2 = int("Input score for first student: ")
score_request_3 = int("Input score for first student: ")
                                                                                                                                                                                                                          