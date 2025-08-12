# Creating and Manipulating Strings
#1-  upper() -converts all characters in the string to uppercase
name = "Ada Balogun"
print(name.upper())

# 2- lower()
sentence = "PYTHON IS AMAZING"
print(sentence.lower())

# 3- strip() - it removes whitespace
text = "   Abuja  "
print(text.strip())


# 4- replace() 
message = "I love Java"
print(message.replace("Java", "Python"))

# 5- swapcase()
text = "hello ABEOKUTA"
print(text.swapcase())

# 6- istrip() - removes whitespace or specified characters from the leftside only
text = "   Nigeria"
print(text.lstrip())

#7- rstrip() 
text = "Nigeria    "
print(text.rstrip())

# 8- split() - splits a string into a list using a separator space
fruits = "mango orange banana"
print(fruits.split())

# 9-  rsplit() - splits a string into a listfrom right side
text = "one,two,three,four"
print(text.rsplit(",", 2))

# 10- splitlines() - splits a string into a list at each newlin(\n)
lines = "Line 1\nLine 2\nLine 3\nLine 4"
print(lines.splitlines())

# 11- join() - joins a list of strings into one string with a specified separator
words = ["I", "Love", "Python"] 
print(" ".join(words))

# 12- center() - centers the string within a specified width,padding with speces or character
text = "Python"
print(text.center(20,"*"))

# 13- ljust -n left-aligns the strings within a specified with,padding and speces or character
test = "Python"
print(text.ljust(10, "*"))

# 14- rjust -  right-aligns the strings within a specified with,padding and speces or character
test = "Python"
print(text.rjust(10, "*"))

# 15- zfill() - pads numeric strings on the left with zeros until it reaches a giv4en lenth
num = "42"
print(num.zfill(5))


# 16- isalpha() - Checks if the stringd contains only letters
print("Lagos".isalpha())  #True
print("Lagos12345".isalpha())  #False

# 17- isdigit() - checks if the string contains only digits
print("1233".isdigit())   #Trus
print("1234Lagos".isdigit())  #false

# 18- isalnum - check if the strings contains only letters and digit
print("Python3".isalnum())  #True

