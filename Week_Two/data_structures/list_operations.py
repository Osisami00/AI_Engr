# List Operation


# 1- Concatenation(+)
    # -joining two list into a new list
    #joins two list into a new list
list1 = [1,2,3]
list2 = [4,5]
result = list2 + list1
print(result)

# Repetition(*)
    # -Repeat elements in a list a given number of lines
nums =[1,2]
repeated = nums * 3
print(repeated)

# 3- indexing
    # Accessing element using their positions(starting from 0)
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[-1])

# 4- Slicing
    # -Extract a portion of the list
numbers = [0,1,2,3,4,5]
print(numbers[1:3])
print(numbers[::-1])
print(numbers[::2])

# 5- Membership (in/nor in)
    # -Check if an element exists in a list
colors = ["red", "green", "blue"]
print("red" in colors)
print("black" in colors)


#6- length (len())
# counts the number of elements in ;list

items = ["pen", "book", "laptop"]
print(len(items))


# 7- Min and Max (min()/max())
    # -Return the smallest or largest element
nums = [5,4,3,2,1]
print(max(nums))
print(max)

# 8- Sum (sum())
    # -add numerical elements in a list\
numbers = [1,2,3,4]
print(sum(numbers))

# 9- list comprehension
    # -create a list in a single line
squares = [x**2 for x in range(5)]
print(squares)

# 10- Copying a list
        # -create duplicate
a = [1,2,3]
b = a.copy()
print(b)
