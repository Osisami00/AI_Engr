# WHAT IS INIT

# __init__ is a special method called a constructor) that automatically runs when you create 
# you create a new object. Think of it as the birth cerificate process - its
# sets up all the basic information about the new obj



# class Student:
#     def __init__(self, name, course, level):  #This runs automatically
#         print("Creating a new student...")
#         self.name = name
#         self.course = course
#         self.level = level
#         print(f"Student {name} has been crerated!")

# # when you create a stude, __init__ runs automatically
# kemi = Student("Kemi", "Computer Science", 300)
# kemi.name = input("Enter your name: ")

# print(kemi.name)


# How INIT and self work together

# class NigerianStudent:
#     def __init__(self, name, state, course):
#         print(f"Step 1: creating student object...")
#         self.name = name
#         self.state_of_origin = state 
#         self.course = course
#         self.student_id = self.generate_id()
#         print(f"Step 6: {self.name} from {self.state_of_origin}, is ready")

#     def generate_id(self):
#         import random 
#         return f"UNISAIL{random.randint(1000,9999)}"

# Michael = NigerianStudent("Michael", "Lagos", "Ai_Engr")
# print(Michael.name)
# print(Michael.student_id)


class PhoneUser:
    def __init__(self, name, network):
        self.name = name
        self.network = network
        self.airtime = 0
        print(f"{self.name} joined {self.network} network")

    def buy_airtime(self, amount):
        self.airtime += amount   #self ensures it goes ton the RIGHT PERSON
        return f"{self.name} now has #{self.airtime} airtime"
    
# creatingmultiple USers
abeeb = PhoneUser("Abeeb Ada", "Airtel")
della = PhoneUser("Della Rae", "MTN")


# eACH PERSONS actions affect only their own account
print(abeeb.buy_airtime(500))          #Abeeb now has 500 airtime
print(della.buy_airtime(3000))         #della now has 3k airtime
print(abeeb.airtime)
print(della.airtime)



# ATTRIBUTES
# Attribute are the characteristics, properties, or data that 
# describe an object. They answer the question "What does this obj "
# "looks like" or "What info does the object store"