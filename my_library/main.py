# main.py - This will be our project entry point

from my_data import data
from my_utils import utils
from services import library


# Add some books
data.add_book("Python Basics", "John Doe")
data.add_book("Advanced Python", "Jane Smith")


# Display All Books
print("Library Collection:")
for b in data.get_books():
    print(utils.format_book(b))

#Borrow a book
print("\nBorrowing a book:")
print(library.borrow_book("Python Basics"))

#Display Books Again
print("\nUpdated Library Collection:")
for b in data.get_books():
    print(utils.format_book(b))
