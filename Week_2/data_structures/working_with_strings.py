# PYTHON DATA STRUCTURE
# 1. String - immutatble sequence of characters(often treated like a sequence)
''''
# Single quotes
name = 'Ada'
print(name)

# Double quotes
greeting = "Hello"
print(greeting)
'''
# Triple quotes (for multi-line strings)
# story = '''Once upon a time,
# there was a coder named Ada.'''
# print(story)


# String with number and symbols
# password = "p@ssw0rd123"
# print(password)

# String Operation
# word = "My name is Michael. I am an engineer"
# print(word[0])  #M
# print(word[-1])  #r

# Slicing
# word = "python"
# print(word[0:4])  #start fro  0 and stop at character 4
# print(word[2:])  #start from 2 then to the end
# print(word[:3])  #start from 0 and stop at 2
# print(word[::2])  #skipper: steps on one character
# print(word[::-1]) #turn words backward

'''
# String Concatenation and Repetition
# Concatenation 
a = "Hello"
b = "World"
print(a + " "+ b) #Hello World

# Repetition
word = "Hi!"
print(word * 3)


# String Searching and Checking
# Membership
text = "Python programming"
print("Python" in text)  #True
print ("Java" not in text)  #False
print ("Java" in text)  #False

# find() / rfind()
text = "Hello Worldooo"
print(text.find("o")) #4
print(text.rfind("o"))  #7  #r-find finds the last element


# index()/rindex()
# (like find() raises an error if not found)
text = "Hello World"
print(text.index("World"))  #6
# print(text.index("Joy")) 
'''

# startswith() / endswith()
filename = "data.csv"
print(filename.startswith("data")) #true
print(filename.endswith("a.csv"))  #true
print(filename.endswith("a.csp"))  #false


