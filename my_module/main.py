import first 
import second

# lets use the funcs in the first.py file

print("=== Math Functions ===")

print("5 + 5 =", first.add(5,3))
print("10 - 4 =", first.subtract(10,4))
print("6 * 7 =", first.multiply(6, 7))
print("20 / 5 =", first.divide(20, 5))


# Lets us the functions in the second.py file
print("\n=== String Fuction ===")
print(second.greet("Michael"))
print("Reverse of 'Python' =", second.reverse_str("Python"))
print("Character count in sentence =", second.count_char("Python modules are powerful"))
print("Word count in sentence =", second.count_words("Python modules are powerful"))
